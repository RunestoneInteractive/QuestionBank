.. activecode::  ch6ex12nq
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
   :pct_on_first: 0.3333333333
   :total_students_attempting: 45
   :num_students_correct: 34.0
   :mean_clicks_to_correct: 3.3235294118

   Finish the code to loop printing the message each time through the loop and remove an ``x`` from the message until all the ``x``'s are gone.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "Ix lovex youxxx";
           System.out.println(message);
   
   
       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     //import java.util.regex.*;
     /* Do NOT change Main or CodeTestHelper.java. */
     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testMain() throws IOException
         {
             String output = getMethodOutput("main");
             String expect = "Ix lovex youxxx\nI lovex youxxx\nI love youxxx\nI love youxx\nI love youx\nI love you\n";
   
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
          @Test
         public void testForLoop()
         {
            String code = getCode();
            boolean passed = code.contains("for") || code.contains("while");
            getResults("Expected loop",""+passed, "Checking for loop",passed);
            assertTrue(passed);
         }
     }