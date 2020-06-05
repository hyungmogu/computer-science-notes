"""
===== Challenge Task 1 of 1 =====

Every one of these GoKarts run on rechargeable battery. The battery provides a
display that shows how charged it can become. There are a total of 8 bars, and
when all bars are lit on the display, the battery is fully charged.

Create a constant that stores the maximum number of energy bars that can be filled.
Use the proper naming structure for your new constant of 'max bars'. Ensure that
the value cannot change, and is accessible from the class level.
"""

class GoKart {
    public static final int MAX_BARS = 8;
    private String color;

    public GoKart(String color) {
      this.color = color;
    }

    public String getColor() {
      return color;
    }

  }
