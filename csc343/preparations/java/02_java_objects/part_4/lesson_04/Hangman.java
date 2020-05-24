
public class Hangman {

    public static void main(String[] args) {
        Game game = new Game("treehouse");
        Prompter prompter = new Prompter(game);

        prompter.displayProgress();

        while (game.getRemainingTries() > 0) {
            boolean isHit = prompter.promptForGuess();
            prompter.displayProgress();
        }
    }

}