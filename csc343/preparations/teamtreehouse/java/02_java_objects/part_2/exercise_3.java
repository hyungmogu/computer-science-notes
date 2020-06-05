"""
===== Challenge Task 1 of 2 =====

Let's expose some helpful properties that are computed using the current state.


Create a new public method named isBatteryEmpty that returns true if the battery
has 0 bars remaining, and false otherwise.
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

    public boolean isBatteryEmpty() {
        return this.barCount == 0;
    }

    public void charge() {
        barCount = MAX_BARS;
    }
}


"""
===== Challenge Task 2 of 2 =====

Great! Now let's create a similar method named isFullyCharged that checks to see if the current bar count is at the
maximum charge.
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

    public boolean isBatteryEmpty() {
        return this.barCount == 0;
    }

    public boolean isFullyCharged() {
        return this.barCount == MAX_BARS;
    }

    public void charge() {
        barCount = MAX_BARS;
    }
}
