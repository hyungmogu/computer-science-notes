import java.util.Arrays;

public class Explore {
    public static void main(String[] args) {
        String[] classmates = {"Ben", "Johnny", "Pasan"};
        String[] classmatesAndMe = new String[4];

        System.arraycopy(classmates, 0, classmatesAndMe, 0, classmates.length);

        System.out.println(Arrays.toString(classmatesAndMe));
    }
}