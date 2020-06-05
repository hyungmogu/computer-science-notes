public class Game {
    private static final int MAX_MISSES = 7;
    private String answer;
    private String hits;
    private String misses;

    public Game(String answer) {
        this.answer = answer;
        this.hits = "";
        this.misses = "";
    }

    public boolean applyGuess(char letter) {
        if (misses.indexOf(letter) != -1 || hits.indexOf(letter) != -1) {
            throw new IllegalArgumentException(letter + " has already been guessed");
        }

        boolean isHit = this.answer.indexOf(letter) != -1;
        if (isHit) {
            hits += letter;
        } else {
            misses += letter;
        }

        return isHit;
    }

    public int getRemainingTries() {
        return MAX_MISSES - this.misses.length();
    }

    public String getCurrentProgress() {
        String progress = "";

        for (char letter : this.answer.toCharArray()) {
            char display = '-';
            boolean hasLetter = this.hits.indexOf(letter) != -1;

            if (hasLetter) {
                display = letter;
            }

            progress += display;
        }

        return progress;
    }
}