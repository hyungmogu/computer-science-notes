import java.io.Console;

public class Explore1 {
    public static void main(String[] args) {
        Console console = System.console();
        // Your amazing code below
        String zipCode = "90210";
        if (zipCode.matches("^\\d{5}(-\\d{4})?$")) {
        System.out.printf("%s is a valid zip code%n", zipCode);
        } else {
        System.out.printf("%s is NOT a valid zip code%n", zipCode);
        }
    }
}