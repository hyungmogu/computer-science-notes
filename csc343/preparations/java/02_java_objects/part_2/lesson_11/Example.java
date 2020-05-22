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

        while (dispenser.dispense()) {
            System.out.println("Chomp!");
        }

        if (dispenser.isEmpty()) {
            System.out.println("Ate all the PEZ");
        }

        dispenser.fill(2);

        while (dispenser.dispense()) {
            System.out.println("Chomp!!");
        }

        try {
            dispenser.fill(400);
            System.out.println("This will never happen");
        } catch(IllegalArgumentException iae) {
            System.out.println("Whoa there!!");
            System.out.printf("The error was %s\n", iae.getMessage());
        }
    }
}