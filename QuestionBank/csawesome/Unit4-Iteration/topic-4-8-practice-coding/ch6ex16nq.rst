.. activecode::  ch6ex16nq
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
   :pct_on_first: 0.4651162791
   :total_students_attempting: 43
   :num_students_correct: 33.0
   :mean_clicks_to_correct: 1.9090909091

   Write a loop below to print the number of ``x``'s in the string message.  Use the ``indexOf`` and ``substring`` methods.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "xyxxzax";
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
             String expect = "4";
   
             boolean passed = output.contains(expect);
             getResults(expect, output, "Expected output from main", passed);
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