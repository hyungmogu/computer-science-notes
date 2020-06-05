"""
===== Challenge Task 1 of 2 =====

Let's use your normalization skills to normalize a discount code for a Shopping Cart application. All codes should be upper
cased, no matter what the user enters

For this first task, create a new private method named normalizeDiscountCode. It should take the discount code that is
passed into the method and return the uppercase version. Call it from the current applyDiscountCode method and set
this.discountCode to the result.
"""


public class Order {
    private String itemName;
    private int priceInCents;
    private String discountCode;

    public Order(String itemName, int priceInCents) {
      this.itemName = itemName;
      this.priceInCents = priceInCents;
    }

    private String normalizeDiscountCode(String discountCode) {
      return discountCode.toUpperCase();
    }

    public String getItemName() {
      return itemName;
    }

    public int getPriceInCents() {
      return priceInCents;
    }

    public String getDiscountCode() {
      return discountCode;
    }

    public void applyDiscountCode(String discountCode) {
      this.discountCode = this.normalizeDiscountCode(discountCode);
    }
  }


"""
===== Challenge Task 2 of 2 =====

Now let's use your validation skills. Only letters and the $ symbols are allowed
in the discount code. Check Example.java for use cases

In the normalizeDiscountCode verify that only letters or the $ character are used.
If any other character is used, throw a IllegalArgumentException with the message
Invalid discount code.
"""

import java.util.regex.*;


public class Order {
    private String itemName;
    private int priceInCents;
    private String discountCode;

    public Order(String itemName, int priceInCents) {
      this.itemName = itemName;
      this.priceInCents = priceInCents;
    }

    private String normalizeDiscountCode(String discountCode) {
      if (Pattern.compile("[^a-zA-Z\\$]").matcher(discountCode).find()) {
        throw new IllegalArgumentException("Invalid discount code");
      }
      return discountCode.toUpperCase();
    }

    public String getItemName() {
      return itemName;
    }

    public int getPriceInCents() {
      return priceInCents;
    }

    public String getDiscountCode() {
      return discountCode;
    }

    public void applyDiscountCode(String discountCode) {
      this.discountCode = this.normalizeDiscountCode(discountCode);
    }
  }
