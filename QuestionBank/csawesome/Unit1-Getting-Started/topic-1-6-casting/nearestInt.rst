.. activecode:: nearestInt
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9964912281
   :total_students_attempting: 855
   :num_students_correct: 855.0
   :mean_clicks_to_correct: 1.0035087719

   Run the code below to see how the formula of adding or subtracting .5 and then casting with (int) rounds a positive or negative double number to the closest int.
   ~~~~
   public class NearestInt
   {
      public static void main(String[] args)
      {
        double number = 5.0 / 3;
        int nearestInt = (int)(number + 0.5);
        System.out.println("5.0/3 = " + number);
        System.out.println("5/3 truncated: " + (int)number );
        System.out.println("5.0/3 rounded to nearest int: " + nearestInt);
        double negNumber = -number;
        int nearestNegInt = (int)(negNumber - 0.5);
        System.out.println("-5.0/3 rounded to nearest negative int: " + nearestNegInt);
      }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "5.0/3 = 1.6666666666666667\n5/3 truncated: 1\n5.0/3 rounded to nearest int: 2\n-5.0/3 rounded to nearest negative int: -2\n";
   
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
     }