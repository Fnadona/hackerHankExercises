import java.util.ArrayList;
import java.util.List;

class Pilha {

    public Pilha(){}

    public static void remove(List<String> pilha){
        int length = pilha.size();
        pilha.remove(length -1);
    }

    public static void adiciona(List<String> pilha, String item){
        pilha.add(item);
    }

    public static List<String> toList(String s){
        int length = s.length();
        List<String> lista = new ArrayList<>();
        for (int i = 0; i<length; i++) {
            if (i != length - 1) {
                lista.add(s.substring(i, i + 1));
            } else lista.add(s.substring(length-1));
        }
        return lista;
    }
}

public class Main {
    public static void main(String[] args){
        List<String> lista = new ArrayList<>();

        Pilha.adiciona(lista, "item 1");
        Pilha.adiciona(lista, "item 2");
        Pilha.adiciona(lista, "item 3");
        Pilha.adiciona(lista, "item 4");
        Pilha.adiciona(lista, "item 5");

        System.out.println(lista);

        Pilha.remove(lista);

        System.out.println(lista);

        System.out.println(Pilha.toList("{[()]}"));

    }
}
