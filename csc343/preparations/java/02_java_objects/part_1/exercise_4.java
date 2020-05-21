"""
===== Challenge Task 1 of 3 =====

Let's ensure that all GoKarts created have a color. We'll solve this over a few
steps.

First, define a public constructor that expects a String argument named color. (Don't worry about adding any code inside
the constructor just yet, we'll do that next.)
"""


class GoKart {
    private String color = "red";

    public GoKart(String color) {

    }

    public String getColor() {
      return color;
    }

  }


"""
===== Challenge Task 2 of 3 =====

Now in the body of your constructor, set the private field color to the value
of the color argument passed into the constructor. (Make sure you are setting the right color*)
"""

class GoKart {
    private String color = "red";

    public GoKart(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

}



"""
===== Challenge Task 3 of 3 =====

Finally, since the color is being set in the constructor now, remove the initialization from the field definition. Just
leave it declared, but not initialized to 'red'.
"""

class GoKart {
    private String color;

    public GoKart(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

}
