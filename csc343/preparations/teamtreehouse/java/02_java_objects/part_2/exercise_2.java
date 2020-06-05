"""
===== Challenge Task 1 of 2 =====

Let's add some state to our GoKart. We'll store the current charge. We'll use the
bars displayed on the battery as the way to know the current charge level

Create a new private field named barCount that will track how many bars of energy
our GoKart battery currently has.
"""

class GoKart {
  public static final int MAX_BARS = 8;
  private String color;
  private int barCount;

  public GoKart(String color) {
    this.color = color;
  }

  public String getColor() {
    return color;
  }
}


"""
===== Challenge Task 2 of 2 =====

Now create a method named charge that sets the new barCount field to the maximum
amount of bars available for each GoKart.
"""


class GoKart {
  public static final int MAX_BARS = 8;
  private String color;
  private int barCount;

  public GoKart(String color) {
    this.color = color;
  }

  public String getColor() {
    return color;
  }

  public void charge() {
    this.barCount = MAX_BARS;
  }
}
