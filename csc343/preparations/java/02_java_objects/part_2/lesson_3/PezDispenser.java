
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

    public void fill() {
        this.pezCount = MAX_PEZ;
        System.out.printf("The current count of delicious PEZ is %d\n", this.pezCount);
    }
}