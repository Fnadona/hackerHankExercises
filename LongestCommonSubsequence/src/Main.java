import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args){
        String sequenceOne = "KEMNL";
        String sequenceTwo = "AFBDG";

        Integer lengthSequenceOne = sequenceOne.length();
        Integer lengthSequenceTwo = sequenceTwo.length();

        String[] listSequenceOne = createList(lengthSequenceOne, sequenceOne);
        String[] listSequenceTwo = createList(lengthSequenceTwo, sequenceTwo);

        System.out.println(LCS(listSequenceOne, listSequenceTwo, lengthSequenceOne, lengthSequenceTwo));

    }

    public static Integer LCS (String[] listOne,
                               String[] listTwo,
                               Integer indexOne,
                               Integer indexTwo){

        if (indexOne == 0 || indexTwo == 0){
            return 0;
        }

        if (listOne[indexOne - 1].equals(listTwo[indexTwo - 1])){
            return  1 + LCS(listOne, listTwo, indexOne - 1, indexTwo - 1);
        } else {
            return  Integer.max(LCS(listOne, listTwo, indexOne, indexTwo - 1),
                    LCS(listOne, listTwo, indexOne - 1, indexTwo));
        }
    }

    public static String[] createList(Integer length, String sequence){

        String[] list = new String[length];

        for(int i = 0; i<length; i++){
            if (i != length - 1){
                list[i] = sequence.substring(i, i+1);
            } else list[i] = sequence.substring(i, length);
        }

        return list;
    }

}
