import java.io.Console;

public class Example {
    public static void main(String[] args) {

        System.out.println("We are making a new PEZ dispenser\n");
        System.out.printf("FUN FACT: There are %d PEZ allowed in every dispenser\n", PezDispenser.MAX_PEZ);

        PezDispenser dispenser = new PezDispenser("Yoda");

        if (dispenser.isEmpty()) {
            System.out.printf("Dispenser is empty");
        }

        System.out.printf("The dispenser is %s\n", dispenser.getCharacterName());

        System.out.printf("Filling the dispenser with delicious PEZ...\n");
        dispenser.fill();

        if (!dispenser.isEmpty()) {
            System.out.printf("Dispenser is full\n");
        }

    }
}