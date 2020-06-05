"""
===== Challenge Task 1 of 2 =====

Making this Hangman game inspired me to try to write one of my favorite board
games, Scrabble. Can you help me using the skills you've learned from the course
thus far? I've modeled a ScrabblePlayer and decided to store their tiles in a
String

For this first task, modify the addTile method so that it appends the tile that
was passed in, to the player's tiles. Practice using the += shortcut method for
string concatenation.
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
      // TODO: Add the tile to tiles
      this.tiles += tile;

    }

    public boolean hasTile(char tile) {
      // TODO: Determine if user has the tile passed in
      return false;
    }

  }


"""
===== Challenge Task 2 of 2 =====

Okay great, now can you fix the hasTile method for me, right now it always returns
false.

Correct the existing hasTile method to return true if the tile is in the tiles
field, and false if it isn't. You can solve this a few ways, however, I'd like
you to practice returning the result of the expression that uses the index of a
char in a String.
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
      // TODO: Add the tile to tiles
      this.tiles += tile;

    }

    public boolean hasTile(char tile) {
      // TODO: Determine if user has the tile passed in
      boolean hasTile = this.tiles.indexOf(tile) != -1;
      return hasTile;
    }

}
