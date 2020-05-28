import java.util.Arrays;

public class Explore1 {
    public static void main(String[] args) {
        Object firstObject = new Object();
        Object secondObject = new Object();

        System.out.println(firstObject == secondObject);

        Object thirdObject = firstObject;

        System.out.println(firstObject == thirdObject);
    }
}