.. activecode:: lcdv3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: F
   :language: java
   :autograde: unittest

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