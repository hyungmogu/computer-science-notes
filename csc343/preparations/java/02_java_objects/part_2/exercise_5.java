"""
===== Challenge Task 1 of 2 =====

Some users of our GoKart class wrote and asked that our drive method accept a
parameter to specify how many laps to go, instead of just one. It happens, well
hey at least you can practice your addition and subtraction shortcuts.

Modify the drive method to define a parameter of how many laps should be driven.
Update the method body to handle the new parameter.
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

    public void drive(int laps) {
      lapsDriven += laps;
      barCount -= laps;
    }
}


"""
===== Challenge Task 2 of 2 =====

Of course, another user of the code just wrote and asked Where'd that drive method
go! I loved that method, can you put it back please? Sigh...Well thanks to method
overloading we can pretty easily bring the method back

Create a new method named drive that accepts no arguments. It should call the newer
drive method passing in a 1 for the default.
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
      this.drive(1);
    }

    public void drive(int laps) {
      lapsDriven += laps;
      barCount -= laps;
    }
  }
