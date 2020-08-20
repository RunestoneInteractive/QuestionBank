.. activecode:: sc2error3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.995157385
   :total_students_attempting: 2478
   :num_students_correct: 2475.0
   :mean_clicks_to_correct: 1.0072727273

   Fix the code below.
   ~~~~
   public class ThirdClass
   {
      public static void main(String[] args)
      {
          system.out.println("Hi there!")
      }
   }
   
   ====
   // should pass if/when they run code
   // This doesn't really work because it filters out the \n
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
   }