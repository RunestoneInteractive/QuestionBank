.. activecode::  ch6ex8nq
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6078431373
   :total_students_attempting: 51
   :num_students_correct: 41.0
   :mean_clicks_to_correct: 1.3902439024

   Finish the code below to print a countdown from 100 to 0 by 10's using a for or while loop.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
   
   
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
         String expect = "100\n90\n80\n70\n60\n50\n40\n30\n20\n10\n0\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
         }
   
          @Test
         public void testForLoop() throws IOException
         {
            String code = getCode();
            boolean passed = code.contains("for") || code.contains("while");
            getResults("Expected loop",""+passed, "Checking for loop",passed);
            assertTrue(passed);
         }
     }