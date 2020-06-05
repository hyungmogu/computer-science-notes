"""
===== Challenge Task 1 of 1 =====

You probably already spotted the error in the drive method that accepts laps.
You can drive way more laps than our battery can handle. Let's fix it. Modify the
drive method to define a parameter of how many laps should be driven.
Update the method body to handle the new parameter.

Add logic to the drive method so that it throws an IllegalArgumentException if
there aren't enough bars to support the laps request. Remember it takes 1 bar of
energy to go around a lap.
"""

class GoKart {
    public static final int MAX_BARS = 8;
    private String color;
    private int barCount;
    private int lapsDriven;

    public GoKart(String color) {
      this.color = color;
    }

    public String getColor() {
      return color;
    }
    public void charge() {
      barCount = MAX_BARS;
    }

    public boolean isBatteryEmpty() {
      return barCount == 0;
    }

    public boolean isFullyCharged() {
      return MAX_BARS == barCount;
    }

    public void drive() {
      drive(1);
    }

    public void drive(int laps) {
       if (barCount < laps) {
        throw new IllegalArgumentException();
       }

      lapsDriven += laps;
      barCount -= laps;
    }
  }