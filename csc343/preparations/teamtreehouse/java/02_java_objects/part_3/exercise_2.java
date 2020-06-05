"""
===== Challenge Task 1 of 1 =====

I've created a tool to help manage lines at tech conferences. The organizers
would like to split the attendees into two lines during the registration process.
I've added notes, examples and a new lesson in the Example.java tab.

Fix the getLineNumberFor method to return a 1 if the first character of lastName
is between A and M or else return 2 if it is between N and Z.
"""


public class ConferenceRegistrationAssistant {

    /**
     * Assists in guiding people to the proper line based on their last name.
     *
     * @param lastName The person's last name
     * @return The line number based on the first letter of lastName
     */
    public int getLineNumberFor(String lastName) {
      int lineNumber = 0;
      /*
        lineNumber should be set based on the first character of the person's last name
        Line 1 - A thru M
        Line 2 - N thru Z

      */

      int ascii = (int) lastName.toUpperCase().charAt(0);

      if (ascii >= 65 && ascii <= 77) {
        return 1;
      } else {
        return 2;
      }
    }

  }
