
public class Hangman {

    public static void main(String[] args) { // <- this guy :)

        if (args.length == 0) {
            System.out.println("Usage: java Hangman <answer>");
            System.err.println("answer is required");
            System.exit(1);
        }

        Game game = new Game(args[0]);
        Prompter prompter = new Prompter(game);

        prompter.displayProgress();

        while (game.getRemainingTries() > 0) {
            prompter.promptForGuess();
            prompter.displayProgress();

            if (game.isWon()) {
                break;
            }
        }
        prompter.displayOutcome();
    }

}