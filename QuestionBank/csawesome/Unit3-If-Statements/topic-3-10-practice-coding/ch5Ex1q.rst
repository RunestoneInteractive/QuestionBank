.. activecode::  ch5Ex1q
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
   :pct_on_first: 0.9848484848
   :total_students_attempting: 66
   :num_students_correct: 66.0
   :mean_clicks_to_correct: 1.0151515152

   The following code should print ``x is greater than 0``.  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 3;
           if (x > 0
               System.out.println("x is greater than 0")
           else
               System.out.println(x is less than or equal 0");
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
             String expect = "x is greater than 0\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }