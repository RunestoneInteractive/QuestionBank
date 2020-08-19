.. activecode::  ch5Ex4q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-10-practice-coding
   :topics: Unit3-If-Statements/topic-3-10-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 1.0
   :total_students_attempting: 54
   :num_students_correct: 54.0
   :mean_clicks_to_correct: 1.0

   The following code should print if x is in the range of 0 to 10 (including 0 and 10). However, the code has errors.  Fix the errors so that the code runs as intended.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 3
           if (x > 0 && x <= 10)
               System.out.println("x is between 0 and 10 inclusive");
           otherwise
               System.out.println("x is either less than 0 or greater than 10");
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
             String expect = "x is between 0 and 10 inclusive\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }