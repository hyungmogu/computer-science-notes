import java.sql.*;
import java.util.Scanner;
import java.util.Arrays;

public class Demo {
    public static void main(String[ ] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Hello Java");
        String minSpeedRaw = myObj.nextLine();
        System.out.println(minSpeedRaw);

        System.out.println("Hello Java 2");
        String minSpeedRaw2 = myObj.nextLine();

        String[] array = minSpeedRaw2.split("-");

        System.out.println(Arrays.toString(array));

        myObj.close();

    }
}