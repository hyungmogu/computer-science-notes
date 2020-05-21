import java.io.Console;

public class Example {
    public static void main(String[] args) {

        System.out.println("We are making a new PEZ dispenser");

        PezDispenser dispenser = new PezDispenser();

        System.out.printf("The dispenser is %s", dispenser.characterName);

    }
}