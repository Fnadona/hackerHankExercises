import java.util.*;

class CountingStrings{
	public static void main(String[] args){
		String[] list = {"the", "get", "bet", "the", "bet"};
		Arrays.sort(list);

		Collections.reverse(Arrays.asList(list));

		System.out.println(Arrays.toString(list));
		System.out.println(Arrays.toString(count(list)));
		System.out.println(Arrays.binarySearch(list, "get"));
	}

	private static int[] count(String[] list){
		int[] intList = new int[ (int ) Arrays.stream(list).distinct().count()];
		String word = list[0];
		int count = 0;
		int j = 0;

		for(int i = 0; i < list.length; i++){
			while(word.equals(list[i])){
				count = count + 1;
				if(i != list.length - 1){
					i = i + 1;
				} else break;
			}
		
			intList[j] = count;
			count = 1;
			word = list[i];
			j = j + 1;
		}

		return intList;
	}
}
