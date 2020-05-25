
public class Hangman {

    public static void main(String[] args) {
        Game game = new Game("treehouse");
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