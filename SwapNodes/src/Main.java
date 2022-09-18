import java.io.*;
import java.lang.reflect.Array;
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

    /*
     * Complete the 'swapNodes' function below.
     *
     * The function is expected to return a 2D_INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. 2D_INTEGER_ARRAY indexes
     *  2. INTEGER_ARRAY queries
     */

    public static List<List<Integer>> swapNodes(List<List<Integer>> indexes, List<Integer> queries) {

        List<List<List<Integer>>> levelList = new ArrayList<>();

        for (int j=0; j < indexes.size(); j++){
            if (j < Math.pow(2,1)){
                System.out.print("Nivel 1: ");
                for (int i = 0; i < Math.pow(2,1); i++){
                    System.out.print(indexes.get(i) + ", ");
                }
                System.out.println("");
                j = 1;
            } else if ((1 < j) && (j < Math.pow(2,2)+j)){
                System.out.print("Nivel 2: ");
                for (int i = j; i < (Math.pow(2,2)+j); i++){
                    System.out.print(indexes.get(i) + ", ");
                }
                System.out.println("");
                j = 5;
            } else if ((5 < j) && (j < Math.pow(2,3) + j)){
                System.out.print("Nivel 3: ");
                for (int i = j; i < Math.pow(2,3) + j; i++){
                    System.out.print(indexes.get(i) + ", ");
                }
                System.out.println("");
                j = 13;
            } else if ((13 < j) && (j < Math.pow(2,4) + j)){
                System.out.print("Nivel 4: ");
                for (int i = j; i < Math.pow(2,4) + j; i++){
                    System.out.print(indexes.get(i) + ", ");
                }
                System.out.println("");
                j = 29;
            } else ;
        }

        return null;
    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> indexes = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            try {
                indexes.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int queriesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> queries = IntStream.range(0, queriesCount).mapToObj(i -> {
                    try {
                        return bufferedReader.readLine().replaceAll("\\s+$", "");
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        List<List<Integer>> result = Result.swapNodes(indexes, queries);

//        result.stream()
//                .map(
//                        r -> r.stream()
//                                .map(Object::toString)
//                                .collect(joining(" "))
//                )
//                .map(r -> r + "\n");
//                .collect(toList());
//                .forEach(e -> {
//                    try {
//                        bufferedWriter.write(e);
//                    } catch (IOException ex) {
//                        throw new RuntimeException(ex);
//                    }
//                });

        bufferedReader.close();
//        bufferedWriter.close();
    }
}

