.. activecode:: challenge1-3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.4017142857
   :total_students_attempting: 1750
   :num_students_correct: 1596.0
   :mean_clicks_to_correct: 2.1860902256

   Working in pairs, debug the following code. Can you find the all the bugs and get the code to run?
   ~~~~
   public class Challenge1_3
   {
      public static void main(String[] args)
      {
          int temperature = 70.5;
          double radioChannel = 101;
          boolean sunny = 1
   
          System.out.print("Welcome to the weather report on Channel ")
          System.out.println(Radiochannel);
          System.out.print("The temperature today is );
          System.out.println(tempurature);
          System.out.print("Is it sunny today? ");
          System.out.println(sunny);
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
        String expect = "Welcome to the weather report on Channel 101 \nThe temperature today is 70.5\nIs it sunny today? true";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
    }
    }