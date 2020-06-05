
public class PezDispenser {
    public static final int MAX_PEZ = 12;
    private final String characterName;

    public PezDispenser(String characterName) {
        this.characterName = characterName;
    }

    public String getCharacterName() {
        return characterName;
    }
}