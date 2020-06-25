import java.sql.*;
import java.util.Scanner;

public class Demo {
    public static void main(String[ ] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Hello Java");
        String minSpeedRaw = myObj.nextLine();
        System.out.println(minSpeedRaw);

        System.out.println("Hello Java 2");
        String minSpeedRaw2 = myObj.nextLine();

        if (minSpeedRaw2.trim().equals("")) {
            System.out.println("white spaces are trimmed!");
        }

        System.out.println(minSpeedRaw2);


    }
}