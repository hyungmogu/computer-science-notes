"""
===== Challenge Task 1 of 3 =====

It's finally time to start allowing our GoKart to drive! Let's keep track of how
many laps each kart drives

First, create a new private int field named lapsDriven.
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
  }


"""
===== Challenge Task 2 of 3 =====

Great! Now let's write a simple drive method. It should be public and not return
anything. We'll start out basic, calling the drive method will make the GoKart
drive a single lap.

In your newly created drive method, increment the new lapsDriven variable by 1.
Use the incrementing shorthand to increase lapsDriven.
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

    public void drive() {
      this.lapsDriven++;
    }

    public boolean isBatteryEmpty() {
      return barCount == 0;
    }

    public boolean isFullyCharged() {
      return MAX_BARS == barCount;
    }
  }



"""
===== Challenge Task 3 of 3 =====

Each lap around the track takes exactly 1 energy bar from the battery.

For this final task, in your drive method, decrement the battery's status that we
maintain in the private field barCount.
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

    public void drive() {
      this.lapsDriven++;
      this.barCount--;
    }

    public boolean isBatteryEmpty() {
      return barCount == 0;
    }

    public boolean isFullyCharged() {
      return MAX_BARS == barCount;
    }
}

