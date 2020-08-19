.. activecode:: ClimbClubA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: climbClubA
   :topics: Unit7-ArrayList/climbClubA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5555555556
   :total_students_attempting: 9
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.8333333333

   Complete the method ``addClimb`` in the ``ClimbingClub`` class in the code below.  The code includes a ``main`` method that will test the ``addClimb`` method.
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
       * * Guaranteed not to be null. Contains only non-null references.
       */
     private List<ClimbInfo> climbList;
   
     /** Creates a new ClimbingClub object. */
     public ClimbingClub()
     {
        climbList = new ArrayList<ClimbInfo>();
     }
   
     /** Adds a new climb with name peakName and time climbTime to the end of the list of climbs
      *
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
       // test a
       ClimbingClub hikerClub = new ClimbingClub();
       hikerClub.addClimb("Monadnock", 274);
       hikerClub.addClimb("Whiteface", 301);
       hikerClub.addClimb("Algonquin", 225);
       hikerClub.addClimb("Monadnock", 344);
       System.out.print(hikerClub);
       System.out.println("The order printed above should be Monadnock, Whiteface, Algonquin, Monadnock");
     }
   
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
   
      public RunestoneTests() {
        super("ClimbingClub");
      }
   
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
   
        String expect = "Peak name: Monadnock time: 274\nPeak name: Whiteface time: 301\nPeak name: Algonquin time: 225\nPeak name: Monadnock time: 344\n";
   
        expect = expect + "The order printed above should be Monadnock, Whiteface, Algonquin, Monadnock\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        ClimbingClub hikerClub = new ClimbingClub();
        hikerClub.addClimb("Monadnock", 274);
        hikerClub.addClimb("Whiteface", 301);
        hikerClub.addClimb("Algonquin", 225);
        hikerClub.addClimb("Monadnock", 344);
   
        String output = hikerClub.toString();
   
        String expect = "Peak name: Monadnock time: 274\nPeak name: Whiteface time: 301\nPeak name: Algonquin time: 225\nPeak name: Monadnock time: 344\n";
   
        boolean result = (output.compareTo(expect) == 0);
   
        boolean passed = getResults("true", ""+result, "addClimb method works with arguments Monadnock: 274, Whiteface:301, Algonquin: 225, Monadnock: 344");
   
        assertTrue(passed);
      }
    }