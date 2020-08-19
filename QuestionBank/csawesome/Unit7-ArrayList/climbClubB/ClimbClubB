.. activecode:: ClimbClubB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: climbClubB
   :topics: Unit7-ArrayList/climbClubB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.125
   :total_students_attempting: 8
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 5.75

   FRQ Climb Club B: complete the method addClimb below.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   
   class ClimbInfo
   {
      private String name;
      private int time;
   
      /** Creates a ClimbInfo object with name peakName and time climbTime.
        *
        * @param peakName the name of the mountain peak
        * @param climbTime the number of minutes taken to complete the climb */
      public ClimbInfo(String peakName, int climbTime)
      {
         name = peakName;
         time = climbTime;
      }
   
      /** @return the name of the mountain peak */
      public String getName()
      {
         return name;
      }
   
      /** @return the number of minutes taken to complete the climb */
      public int getTime()
      {
         return time;
      }
   
      public String toString()
      {
         return "Peak name: " + name + " time: " + time;
      }
   }
   
   public class ClimbingClub
   {
      /** The list of climbs completed by members of the club.
        *  Guaranteed not to be null. Contains only non-null references.
        */
      private List<ClimbInfo> climbList;
   
      /** Creates a new ClimbingClub object. */
      public ClimbingClub()
      {
         climbList = new ArrayList<ClimbInfo>();
      }
   
      /** Adds a new climb with name peakName and time climbTime
        * to the list of climbs in order by name
        * @param peakName the name of the mountain peak climbed
        * @param climbTime the number of minutes taken to complete the climb
        */
      public void addClimb(String peakName, int climbTime)
      {
   
      }
   
      public String toString()
      {
         String output ="";
         for (ClimbInfo info : climbList)
         {
            output = output + info.toString() + "\n";
         }
         return output;
      }
   
      public static void main(String[] args)
      {
         ClimbingClub hikerClub = new ClimbingClub();
         hikerClub.addClimb("Monadnock", 274);
         hikerClub.addClimb("Whiteface", 301);
         hikerClub.addClimb("Algonquin", 225);
         hikerClub.addClimb("Monadnock", 344);
         System.out.print(hikerClub);
         System.out.println("The order printed above should be Algonquin, Monadnock, Monadnock, Whiteface");
      }
   
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
   
       public RunestoneTests()
       {
         super("ClimbingClub");
       }
   
   
       @Test
       public void testMain() throws IOException
       {
         String output = getMethodOutput("main");
   
         String expect1 = "The order printed above should be Algonquin, Monadnock, Monadnock, Whiteface";
   
         boolean passed = output.contains(expect1);
   
         getResults(expect1, output, "Expected output from main", passed);
   
         assertTrue(passed);
         }
   
      @Test
       public void test1()
       {
         ClimbingClub hikerClub = new ClimbingClub();
         hikerClub.addClimb("Mount B", 200);
         hikerClub.addClimb("Mount C", 300);
         hikerClub.addClimb("Mount A", 225);
   
         String output = hikerClub.toString();
   
         String expect1 = "Peak name: Mount A time: 225\nPeak name: Mount B time: 200\nPeak name: Mount C time: 300";
   
         boolean passed = (getResults(expect1, output, "addClimb on new input with sorting works"));
         assertTrue(passed);
       }
     }