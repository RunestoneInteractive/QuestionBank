.. activecode::  ch6ex7nq
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
   :pct_on_first: 0.66
   :total_students_attempting: 50
   :num_students_correct: 41.0
   :mean_clicks_to_correct: 1.1951219512

   The following code should print the values from 10 to 1, but it has errors.  Fix the errors so that the code works as intended.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 10;
           while (x >= 0)
           {
              x--;
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
             String expect = "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n";
   
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }