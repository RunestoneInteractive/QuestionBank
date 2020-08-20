.. activecode::  ch6ex9nq
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
   :pct_on_first: 0.3541666667
   :total_students_attempting: 48
   :num_students_correct: 37.0
   :mean_clicks_to_correct: 2.3513513514

   Finish the following code so that it prints a string message minus the last character each time through the loop until there are no more characters in message.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
              String message = "help";
   
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
             String expect = "help\nhel\nhe\nh\n";
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