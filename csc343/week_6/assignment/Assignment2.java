import java.sql.*;
import java.util.Date;
import java.text.SimpleDateFormat;

// If you are looking for Java data structures, these are highly useful.
// Remember that an important part of your mark is for doing as much in SQL (not Java) as you can.
// Solutions that use only or mostly Java will not received a high mark.
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Assignment2 {

   // A connection to the database
   Connection connection;

   Assignment2() {}

  /**
   * Connects and sets the search path.
   *
   * Establishes a connection to be used for this session, assigning it to
   * the instance variable 'connection'.  In addition, sets the search
   * path to bnb.
   *
   * @param  url       the url for the database
   * @param  username  the username to connect to the database
   * @param  password  the password to connect to the database
   * @return           true if connecting is successful, false otherwise
   */
   public boolean connectDB(String URL, String username, String password) {
        // WRITE HERE
   }


  /**
   * Closes the database connection.
   *
   * @return true if the closing was successful, false otherwise
   */
   public boolean disconnectDB() {
        // WRITE HERE
   }


   /**
    * Returns the 10 most similar homeowners based on traveller reviews.
    *
    * Does so by using Cosine Similarity: the dot product between the columns
    * representing different homeowners. If there is a tie for the 10th
    * homeowner (only the 10th), more than 10 records may be returned.
    *
    * @param  homeownerID   id of the homeowner
    * @return               a list of the 10 most similar homeowners
    */
    // public HashMap homeownerRecommendation(int homeownerID) {
    public ArrayList homeownerRecommendation(int homeownerID) {
        // WRITE HERE
    }

   /**
    * Records the fact that a booking request has been accepted by a
    * homeowner.
    *
    * If a booking request was made and the corresponding booking has not been
    * recorded, records it by adding a row to the Booking table, and returns
    * true. Otherwise, returns false.
    *
    * @param  requestID  id of the booking request
    * @param  start      start date for the booking
    * @param  numNights  number of nights booked
    * @param  price      amount paid to the homeowner
    * @return            true if the operation was successful, false otherwise
    */
    public boolean booking(int requestId, Date start, int numNights, int price) {
        // WRITE HERE
    }



   public static void main(String[] args) {
    /*
    You can put testing code in here. It will not affect our autotester.
        Note to self: to run this program:
        'javac Assignment2.java'
        'java -cp /local/packages/jdbc-postgresql/postgresql-9.4.1212.jar: Assignment2'
    */
        try {
            Assignment2 a2 = new Assignment2();
            String url = "jdbc:postgresql://localhost:5432/csc343h-ngsunny";
            a2.connectDB(url,"ngsunny","");

            // a2.homeownerRecommendation(4000);
            // SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd");
            // a2.booking(6000, ft.parse("2016-10-05"), 2, 120);

            a2.disconnectDB();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

}
