def buildingGridAfterExplosion(grid, bombPosition):

	for bomb in bombPosition:
		grid[bomb[0]][bomb[1]] = "."

		if(bomb[0] > 0):
			grid[bomb[0] - 1][bomb[1]] = "."

		if(bomb[1] > 0):
			grid[bomb[0]][bomb[1] - 1] = "."

		if(bomb[0] + 1 < len(grid)):
			grid[bomb[0] + 1][bomb[1]] = "."
		
		if(bomb[1] + 1 < len(grid[0])):
			grid[bomb[0]][bomb[1] + 1] = "."

def searchingForBombs(grid, bombPosition):

	for row in range(0,len(grid)):
		for col in range(0,len(grid[0])):
			if(grid[row][col] == "O"):
				bombPosition.append([row,col])

def buildingResponse(grid):
	responseGrid = []

	for row in range(len(grid)):
		string = ""

		for col in range(len(grid[0])):
			string = string + grid[row][col]

		responseGrid.append(string)

	return responseGrid

def bomberMan(n,grid):

	if(n == 1):
		return grid

	if(n % 2 == 0):
		return ["O"*len(grid[0])]*len(grid)

	firstBombPositions = []
	secondBombPositions = []	
	
	secondGrid = [["O" for j in range(len(grid[0]))] for i in range(len(grid))]
	thirdGrid = [["O" for j in range(len(grid[0]))] for i in range(len(grid))]
	
	searchingForBombs(grid, firstBombPositions)
	buildingGridAfterExplosion(secondGrid, firstBombPositions)
	searchingForBombs(secondGrid, secondBombPositions)
	buildingGridAfterExplosion(thirdGrid, secondBombPositions)
	
	if(n % 4 == 3):
		return buildingResponse(secondGrid)
	else:
		return buildingResponse(thirdGrid)

n = 11
grid = [".......","...O.O.","....O..","..O....","OO...OO","OO.O..."]

print(bomberMan(n,grid))
