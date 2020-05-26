"""
===== Challenge Task 1 of 1 =====

Let's use your normalization skills to normalize a discount code for a Shopping Cart application. All codes should be upper
cased, no matter what the user enters

For this first task, create a new private method named normalizeDiscountCode. It should take the discount code that is
passed into the method and return the uppercase version. Call it from the current applyDiscountCode method and set
this.discountCode to the result.
"""

public class Programmers {

    public void printMenu() {
      String[] programmers = {
              "Yukihiro Matsumoto",
              "David Nolen",
              "Grace Hopper",
              "Linus Torvalds",
              "You"
      };

      System.out.println("Choose a programmer:");
      // TODO: Print out a menu by looping through the programmers array.
      /*
        The menu should be in the form of (each on a line of its own, starting with 1):
        1. Yukihiro Matsumoto
        2. David Nolen
        ...
      */
      for (int i = 0; i < programmers.length; i ++) {
        String programmer = programmers[i];
        System.out.printf("%d. %s\n", i+1, programmer);
      }

    }

  }
