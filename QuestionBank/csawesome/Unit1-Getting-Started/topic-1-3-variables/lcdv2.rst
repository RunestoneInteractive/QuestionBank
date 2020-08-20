.. activecode:: lcdv2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.995472837
   :total_students_attempting: 1988
   :num_students_correct: 1988.0
   :mean_clicks_to_correct: 1.004527163

   Run the following code to see what is printed. Then, change the values and run it again. Try adding quotes to variables and removing spaces in the print out statements to see what happens.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        int score;
        score = 0;
        System.out.print("The score is ");
        System.out.println(score);
   
        double price = 23.25;
        System.out.println("The price is " + price);
   
        boolean won = false;
        System.out.println(won);
        won = true;
        System.out.println(won);
   
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
            String expect = "The score is 0\nThe price is 23.25\nfalse\ntrue\nHi Jose";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
   }