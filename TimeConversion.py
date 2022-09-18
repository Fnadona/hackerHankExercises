s = "12:40:22AM"

timeSplited = s.split(":")
isAM = timeSplited[2].endswith("AM")

if(isAM):
	if(timeSplited[0] == "12"):
		hour = "00"
	else:
        	hour = timeSplited[0]
        
	print(str(hour) + ":" + timeSplited[1] + ":" + timeSplited[2].split("AM")[0])
else:
	if(timeSplited[0] == "12"):
		hour = timeSplited[0]
	else:
		hour = int(timeSplited[0]) + 12
    
	print(str(hour) + ":" + timeSplited[1] + ":" + timeSplited[2].split("PM")[0])
