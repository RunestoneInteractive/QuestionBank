.. activecode::  ch6ex4q
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
   :pct_on_first: 0.56
   :total_students_attempting: 50
   :num_students_correct: 40.0
   :mean_clicks_to_correct: 1.45

   Rewrite the following code to use a ``while`` loop instead of a ``for`` loop to print out the numbers from 10 to 100 by 10's (inclusive).
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           for (int x = 10; x <= 100; x=x+10)
               System.out.println(x);
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
             String expect = "10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n";
   
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
         @Test
         public void testForLoop() throws IOException
         {
             String target = "while (x";
             boolean passed = checkCodeContains("while loop", target);
             assertTrue(passed);
         }
     }