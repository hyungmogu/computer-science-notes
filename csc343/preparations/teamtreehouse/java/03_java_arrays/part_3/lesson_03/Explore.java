import java.util.Arrays;
import java.util.Comparator;

public class Explore {
    public static void main(String[] args) {
        String[] classmates = {"Ben", "Johnny", "Pasan"};

        Arrays.sort(classmates, Comparator.comparing(String::length)); // <- sorts based on length of string
        System.out.println(Arrays.toString(classmates));

        // Returns ["Ben", "Pasan", "Johnny"]
    }
}