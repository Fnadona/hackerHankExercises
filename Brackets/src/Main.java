import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static void remove(List<String> pilha){
        pilha.remove(pilha.size()-1);
    }

    public static void adiciona(List<String> pilha, String item){
        pilha.add(item);
    }

//    public static List<String> toList(String s){
//        int length = s.length();
//        List<String> lista = new ArrayList<>();
//        for (int i = 0; i<length; i++) {
//            if (i != length - 1) {
//                lista.add(s.substring(i, i + 1));
//            } else lista.add(s.substring(length-1));
//        }
//        return lista;
//    }

    public static String isBalanced(String s) {
        int length = s.length();
        int index = 0;
        int i = 1;
        List<String> list = new ArrayList<>();

        if(length % 2 != 0 || length == 0){
            return "NO";
        } else {
            adiciona(list, String.valueOf(s.charAt(0)));
            while(i<length){

                if (list.isEmpty()){
                    adiciona(list, String.valueOf(s.charAt(i)));
                    System.out.println(list);
                    index = list.size() - 1;
                    i++;
                    continue;
                } else if (list.get(index).equals("{")) {
                    if (String.valueOf(s.charAt(i)).equals("}")){
                        remove(list);

                        if (!list.isEmpty()) index = list.size() - 1;
                        else index = 0;

                        i++;
                        System.out.println(list);
                        continue;
                    }
                } else if (list.get(index).equals("[")) {
                    if (String.valueOf(s.charAt(i)).equals("]")){
                        remove(list);

                        if (!list.isEmpty()) index = list.size() - 1;
                        else index = 0;

                        i++;
                        System.out.println(list);
                        continue;
                    }
                } else if (list.get(index).equals("(")) {
                    if (String.valueOf(s.charAt(i)).equals(")")){
                        remove(list);

                        if (!list.isEmpty()) index = list.size() - 1;
                        else index = 0;

                        i++;
                        System.out.println(list);
                        continue;
                    }
                }
                adiciona(list, String.valueOf(s.charAt(i)));
                System.out.println(list);
                index = list.size() - 1;
                i++;
            }

            if (list.isEmpty()) return "YES";
            else return "NO";
        }
    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String s = bufferedReader.readLine();

                String result = Result.isBalanced(s);

                System.out.println(result);
//                bufferedWriter.write(result);
//                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
//        bufferedWriter.close();
    }
}

