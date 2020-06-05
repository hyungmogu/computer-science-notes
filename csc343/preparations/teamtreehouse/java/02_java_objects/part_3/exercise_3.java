"""
===== Challenge Task 1 of 2 =====

Okay, so I need to count how many occurrences of a a specific letter is in the
player's tiles. Let's build that over a couple of steps. I've added some example
use cases in Example.java

Create a new method named getCountOfLetter that returns an int, and requires a parameter of type char named letter. For
this task, just make it return 0.
"""


public class ScrabblePlayer {
    // A String representing all of the tiles that this player has
    private String tiles;

    public ScrabblePlayer() {
      tiles = "";
    }

    public String getTiles() {
      return tiles;
    }

    public void addTile(char tile) {
      tiles += tile;
    }

    public boolean hasTile(char tile) {
      return tiles.indexOf(tile) != -1;
    }

    public int getCountOfLetter(char letter) {
        return 0;
    }
  }


"""
===== Challenge Task 2 of 2 =====

You'll need to use your skills to loop through each of the tiles, use an equality check, and then increment a counter if
the tile and letter match. You got this!


Now in your new method, have it return a number representing the count of tiles
that match the letter that was passed in to the method. Make sure to check Example.java
for some example uses.
"""


public class ScrabblePlayer {
    // A String representing all of the tiles that this player has
    private String tiles;

    public ScrabblePlayer() {
      tiles = "";
    }

    public String getTiles() {
      return tiles;
    }

    public void addTile(char tile) {
      tiles += tile;
    }

    public boolean hasTile(char tile) {
      return tiles.indexOf(tile) != -1;
    }

    public int getCountOfLetter(char letter) {
        int count = 0;

        for (char tile : this.tiles.toCharArray()) {
            if(tile == letter) {
                count++;
            }
        }

        return count;
    }
  }
