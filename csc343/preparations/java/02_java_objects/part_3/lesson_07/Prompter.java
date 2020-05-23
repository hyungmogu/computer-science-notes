import java.util.Scanner;

public class Prompter {
    private Game game;

    public Prompter(Game game) {
        this.game = game;
    }

    public boolean promptForGuess() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a letter: ");
        String guessInput = scanner.nextLine();
        char guess = guessInput.charAt(0);
        return game.applyGuess(guess);
    }
}