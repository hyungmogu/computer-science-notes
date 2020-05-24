public class Game {
    private static final int MAX_MISSES = 7;
    private String answer;
    private String hits;
    private String misses;

    public Game(String answer) {
        this.answer = answer.toLowerCase();
        this.hits = "";
        this.misses = "";
    }

    private char normalizeGuess(char letter) {
        if (! Character.isLetter(letter)) {
            throw new IllegalArgumentException("A letter is Required");
        }
        letter = Character.toLowercase(letter);

        if (misses.indexOf(letter) != -1 || hits.indexOf(letter) != -1) {
            throw new IllegalArgumentException(letter + "has already been guessed");
        }

        return letter;
    }

    public boolean applyGuess(char letter) {
        letter = normalizeGuess(letter);
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