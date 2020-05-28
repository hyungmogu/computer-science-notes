import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Explore3 {
    public static void main(String[] args) {
        String script = "Procrastination is surely not the destination, should we talk about shiny things?";

        Pattern pattern = Pattern.compile("(\\w*(sh|ti|su)\\w*)",
                                          Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(script);

        while (matcher.find()) {
            System.out.printf("%s is a shushy word because of %s \n",
                              matcher.group(1), // <- returns value of outer parenthesis
                              matcher.group(2)); // <- returns value of inner parenthesis
        }
    }
}