import java.util.Arrays;

public class Explore4 {
    public static void main(String[] args) {
        String firstObject = "String";
        String secondObject = new String("String").intern();

        System.out.println(firstObject == secondObject); // <- Returns true
    }
}