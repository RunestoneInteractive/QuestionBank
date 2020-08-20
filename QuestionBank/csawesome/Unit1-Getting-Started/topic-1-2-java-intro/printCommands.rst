.. activecode:: printCommands
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3443952802
   :total_students_attempting: 2712
   :num_students_correct: 2502.0
   :mean_clicks_to_correct: 2.0575539568

   Run this code to see the output below it. How would you change it to print the ! on the same line as Hi there keeping all 3 print statements?
   ~~~~
   public class MyClass
   {
      public static void main(String[] args)
      {
          System.out.print("Hi ");
          System.out.println("there");
          System.out.print("!");
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
            String expect = "Hi there!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void testLineCount() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "1 output line";
            String actual = "  output line";
   
            if (output.length() > 0) {
               actual = output.split("\n").length + actual;
            } else {
               actual = output.length() + actual;
           }
           boolean passed = getResults(expect, actual, "Checking lines of output");
           assertTrue(passed);
        }
   }