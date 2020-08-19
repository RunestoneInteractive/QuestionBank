.. activecode::  ch5Ex5q
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
   :pct_on_first: 0.4333333333
   :total_students_attempting: 60
   :num_students_correct: 50.0
   :mean_clicks_to_correct: 2.2

   The following code should print if x is less than 0, equal to 0, or greater than 0.  Finish it to work correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = -3;
           if (x > 0)
               System.out.println("x is less than 0");
   
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
           String expect = "x is less than 0";
           boolean passed = getResults(expect, output, "Expected output from main if x = -3");
           assertTrue(passed);
         }
   
         @Test
         public void testCheckCodeContains()
         {
             boolean outputLess = checkCodeContains("if (x < 0)");
             assertTrue(outputLess);
         }
         @Test
         public void testCheckCodeContains2()
         {
             String code = getCode();
             boolean ifGreater = code.contains("if (x > 0)");
             boolean ifEqual = code.contains("if (x == 0)");
             boolean passed = getResults("Test if x greater than 0 or test if x is equal to 0", "Greater than: " + ifGreater + ", Equal to: " + ifEqual, "Test if x greater than 0 or if x equal to 0", ifGreater || ifEqual );
             assertTrue(passed);
         }
     }