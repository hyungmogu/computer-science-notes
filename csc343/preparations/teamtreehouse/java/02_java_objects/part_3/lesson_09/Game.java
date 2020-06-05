public class Game {
    private String answer;
    private String hits;
    private String misses;

    public Game(String answer) {
        this.answer = answer;
        this.hits = "";
        this.misses = "";
    }

    public boolean applyGuess(char letter) {
        boolean isHit = this.answer.indexOf(letter) != -1;
        if (isHit) {
            hits += letter;
        } else {
            misses += letter;
        }

        return isHit;
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