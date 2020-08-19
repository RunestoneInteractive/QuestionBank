.. activecode:: lcdv3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.984508547
   :total_students_attempting: 1872
   :num_students_correct: 1870.0
   :mean_clicks_to_correct: 1.0171122995

   This is an example of *assignment dyslexia*, when the coder has put the value on the left and the declaration on the right side.  Try to fix the following code to compile and run.
   ~~~~
   public class Test3
   {
      public static void main(String[] args)
      {
        int score;
        4 = score;
        System.out.println(score);
      }
   }
   
   ====
   // should pass if/when they run code
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;
   
   public class RunestoneTests extends CodeTestHelper
   {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "4";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }