
public class PezDispenser {
    public static final int MAX_PEZ = 12;
    private final String characterName;
    private int pezCount;

    public PezDispenser(String characterName) {
        this.characterName = characterName;
        this.pezCount = 0;
    }

    public String getCharacterName() {
        return characterName;
    }

    public boolean isEmpty() {
        return this.pezCount == 0;
    }

    public boolean dispense() {
        boolean wasDispensed = false;
        if (!this.isEmpty()) {
            this.pezCount--;
            wasDispensed = true;
        }

        return wasDispensed;

    }

    public void fill() {
        this.fill(MAX_PEZ);
    }

    public void fill(int pezAmount) {
        this.pezCount = pezAmount;
        System.out.printf("The current count of delicious PEZ is %d\n", this.pezCount);
    }

}