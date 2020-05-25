"""
===== Challenge Task 1 of 4 =====

Can I please borrow your object powers to help me finish out this Forum prototype
I've been working on? We'll go through a couple of steps here, like always, just
follow the prompts for each step. Let's do this!

For this first task, create a new private method named normalizeDiscountCode. It should take the discount code that is
passed into the method and return the uppercase version. Call it from the current applyDiscountCode method and set
this.discountCode to the result.
"""


// Forum.java
public class Forum {
    private String topic;

    // TODO: add a constructor that accepts a topic and sets the private field topic
    public Forum(String topic) {
      this.topic = topic;
    }

    public String getTopic() {
      return topic;
    }


    /* Uncomment this when you are prompted to do so
    public void addPost(ForumPost post) {
      System.out.printf("A new post in %s topic from %s %s about %s is available",
              topic,
              post.getAuthor().getFirstName(),
              post.getAuthor().getLastName(),
              post.getTitle()
      );
    }
    */

  }


"""
===== Challenge Task 2 of 4 =====

I didn't get too far on the User object, sorry :( I left some TODOs in there that
should help...

In User.java, add private fields to store firstName and lastName, and initialize
them in the provided constructor. Add public getters for firstName and lastName.
"""


// Forum.java
public class Forum {
    private String topic;

    // TODO: add a constructor that accepts a topic and sets the private field topic
    public Forum(String topic) {
      this.topic = topic;
    }

    public String getTopic() {
      return topic;
    }


    /* Uncomment this when you are prompted to do so
    public void addPost(ForumPost post) {
      System.out.printf("A new post in %s topic from %s %s about %s is available",
              topic,
              post.getAuthor().getFirstName(),
              post.getAuthor().getLastName(),
              post.getTitle()
      );
    }
    */

  }


// User.java
public class User {
    // TODO: add private fields for firstName and lastName
    private String firstName;
    private String lastName;

    public User(String firstName, String lastName) {
      // TODO: set and add the private fields
      this.firstName = firstName;
      this.lastName = lastName;
    }

    // TODO: add getters for firstName and lastName
    public String getFirstName() {
      return this.firstName;
    }

     public String getLastName() {
      return this.lastName;
    }
  }


"""
===== Challenge Task 3 of 4 =====

Okay so now let's work on ForumPost.java

Add a constructor to ForumPost which accepts a User named author, a String named
title, and another String named description. Initialize the corresponding private
fields.
"""

// ForumPost.java
public class ForumPost {
    private User author;
    private String title;
    private String description;

    // TODO: add a constructor that accepts the author, title and description
    public ForumPost(User author, String title, String description) {
      this.author = author;
      this.title = title;
      this.description = description;
    }

    public User getAuthor() {
      return author;
    }

    public String getTitle() {
      return title;
    }

    public String getDescription() {
      return description;
    }
  }



"""
===== Challenge Task 4 of 4 =====

So close now! Okay so now un-comment the comments in Main.java and Forum.java.
PS. You're awesome!

After you uncomment the code in Main.java and Forum.java, fix the code as described
in the comments of Main.java. The code in main is attempting to use the code you
just fixed.
"""


//Main.java
public class Main {

    public static void main(String[] args) {
      System.out.println("Beginning forum example");
      if (args.length < 2) {
        System.out.println("Usage: java Main <first name> <last name>");
        System.err.println("<first name> and <last name> are required");
        System.exit(1);
      }

      String firstName = args[0];
      String lastName = args[1];

      Forum forum = new Forum("Java");
      // TODO: pass in the first name and last name that are in the args parameter
      User author = new User(firstName, lastName);
      // TODO: initialize the forum post with the user created above and a title and description of your choice
      ForumPost post = new ForumPost(author, "corgi", "the little dog");
      forum.addPost(post);

    }

  }

// Forum.java
public class Forum {
    private String topic;

    // TODO: add a constructor that accepts a topic and sets the private field topic
    public Forum(String topic) {
        this.topic = topic;
    }

    public String getTopic() {
        return topic;
    }

    public void addPost(ForumPost post) {
        System.out.printf("A new post in %s topic from %s %s about %s is available",
                topic,
                post.getAuthor().getFirstName(),
                post.getAuthor().getLastName(),
                post.getTitle()
        );
    }
}
