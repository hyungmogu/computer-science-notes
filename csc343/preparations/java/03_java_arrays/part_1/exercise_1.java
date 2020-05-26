"""
===== Challenge Task 1 of 1 ======

In the class TeachersExamples there are two methods. One shows a longer version
of how to create an array. Your task is to create the array in a shorter literal
form in the method getTeachersAsArrayLiteral, replacing the null assignment.
"""

public class TeachersExample {

    public String[] getTeachersInArrayLongForm() {
      String[] teachers = new String[3];
      teachers[0] = "Jay";
      teachers[1] = "Dave";
      teachers[2] = "James";
      return teachers;
    }

    public String[] getTeachersAsArrayLiteral() {
      // TODO: Replace null with an array literal that matches the long form above
      String[] teachers = {"Jay", "Dave", "James"};
      return teachers;
    }

  }
