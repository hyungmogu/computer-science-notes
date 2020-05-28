import java.io.Console;

public class Explore2 {
    public static void main(String[] args) {
        String skills = "JavaScript, HTML, CSS, and Java";
        for (String skill : skills.split("\\W+(and\\W+)?")) {
            System.out.printf("Skill : %s \n", skill);
        }
    }
}