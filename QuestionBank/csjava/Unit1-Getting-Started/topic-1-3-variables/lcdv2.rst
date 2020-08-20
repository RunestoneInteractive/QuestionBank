.. activecode:: lcdv2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: F
   :language: java
   :autograde: unittest

   Run the following code to see what is printed.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        int score;
        score = 0;
        System.out.println("The score is " + score);

        double price = 23.25;
        System.out.println("The price is " + price);

        boolean won = false;
        System.out.println("Won? " + won);
        won = true;
        System.out.println("Won? " + won);

        String name = "Jose";
        System.out.println("Hi " + name);
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
            String expect = "The score is 0\nThe price is 23.25\nWon? false\nWon? true\nHi Jose";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
   }