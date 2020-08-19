.. activecode::  ch6ex5q
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
   :pct_on_first: 0.5490196078
   :total_students_attempting: 51
   :num_students_correct: 42.0
   :mean_clicks_to_correct: 1.5952380952

   The following code should print the values from 1 to 10 (inclusive) but has errors.  Fix the errors so that the code works as intended. If the code is in an infinite loop you can refresh the page in the browser to stop the loop and then click on Load History and move the bar above it to see your last changes.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 1;
           while (x < 10)
           {
               System.out.println(x);
           }
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
         String expect = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
         @Test
         public void testWhileLoop() throws IOException
         {
             String target1 = "x=x+1;";
             String target2 = "x++;";
             String code = removeSpaces(getCode());
             boolean passed = code.contains(target1) || code.contains(target2);
             getResults("true", ""+passed, "changing the loop variable");
             assertTrue(passed);
         }
     }