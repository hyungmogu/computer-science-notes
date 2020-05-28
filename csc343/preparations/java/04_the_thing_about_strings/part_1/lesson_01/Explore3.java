import java.util.Arrays;

public class Explore3 {
    public static void main(String[] args) {
        String firstObject = "String";
        String secondObject = new String("String");

        System.out.println(firstObject == secondObject); // <- Returns false
    }
}