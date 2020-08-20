.. activecode:: code1_3_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: T
   :language: java
   :autograde: unittest

   Run the following code to see what is printed.
   Then, change the values and run it again.

   Click the ``Show CodeLens`` button and then use the ``Next`` button to step through the
   program one line at a time.  Stepping through a program lets you see how memory is assigned for each variable.

   ~~~~
   public class VariableAssignment
   {
      public static void main(String[] args)
      {
        int score;
        score = 4;
        System.out.println(score);

        double price = 23.25;
        System.out.println(price);

        boolean won = false;
        System.out.println(won);
        won = true;
        System.out.println(won);

        String name = "Jose";
        System.out.println(name);
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
            String expect = "4\n23.25\nfalse\ntrue\nJose";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
   }