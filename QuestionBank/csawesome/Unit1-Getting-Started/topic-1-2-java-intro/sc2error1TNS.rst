.. activecode:: sc2error1TNS
   :author: Tiffani Slutsky
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.9891304348
   :total_students_attempting: 92
   :num_students_correct: 92.0
   :mean_clicks_to_correct: 1.0108695652

   Fix the code below.
   ~~~~
   public class FirstClass
   {
      public static void main(String[] args)
      {
         System.out.println("Hi there!);
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
            String expect = "Hi there!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }