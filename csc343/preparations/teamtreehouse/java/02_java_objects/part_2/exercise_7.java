"""
===== Challenge Task 1 of 1 =====

Example.java contains a program using the GoKart class we have been building
(included for you to reference).

Protect the call to kart.drive by handling the IllegalArgumentException that is
hrown when not enough battery remains. Print out the message from the exception
to the screen as you catch the exception.
"""

class Example {

    public static void main(String[] args) {
      GoKart kart = new GoKart("purple");
      if (kart.isBatteryEmpty()) {
        System.out.println("The battery is empty");
      }
      try {
        kart.drive(42);
      } catch (IllegalArgumentException iae) {
        System.out.println(iae.getMessage());
      }
    }

  }
