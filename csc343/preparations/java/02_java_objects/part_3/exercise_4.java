"""
===== Challenge Task 1 of 2 =====

Oooh with the new skills we can build a little Twitter like app. I've created a
new tweet class, let's write the 140 characters story.

Add a new constant that defines the max chars allowed and set it 140. Use proper
case for constants. Ensure it is accessible off the class, and that it cannot be
changed.
"""

public class Tweet {
    public static final int MAX_CHARS = 140;
    private String text;

    public Tweet(String text) {
      this.text = text;
    }

    public String getText() {
      return text;
    }

    public void setText(String text) {
      this.text = text;
    }
  }


"""
===== Challenge Task 2 of 2 =====

Let's let them know how many characters they have left to use...so they can jam
them full of hashtags #jklol

Create a public method named getRemainingCharacterCount that returns an int
representing how many characters they have left before they 140. Base your
calculation on the field that stores the current text.
"""


public class Tweet {
    public static final int MAX_CHARS = 140;
    private String text;

    public Tweet(String text) {
      this.text = text;
    }

    public String getText() {
      return text;
    }

    public int getRemainingCharacterCount() {
      return MAX_CHARS - this.text.length();
    }

    public void setText(String text) {
      this.text = text;
    }
}

