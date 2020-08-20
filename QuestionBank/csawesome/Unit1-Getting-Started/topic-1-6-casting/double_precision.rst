.. activecode:: double_precision
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9969924812
   :total_students_attempting: 665
   :num_students_correct: 665.0
   :mean_clicks_to_correct: 1.0030075188

   Run the code below to see how a decimal number can be formatted to show 2 digits after the decimal point.
   ~~~~
   public class TestFormat
   {
      public static void main(String[] args)
      {
        double number = 10 / 3;
        System.out.println(number);
        System.out.println( String.format("%.02f", number) );
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "3.0\n3.00\n";
   
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }