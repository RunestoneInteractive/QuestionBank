.. activecode::  ch6ex6q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   The following code should print the values from 10 to 5, but it has errors.  Fix the errors so that the code works as intended.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           for (int x = 10; x >= 5; x--)
           {
              System.out.println(x);
              x--;
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
             String expect = "10\n9\n8\n7\n6\n5\n";

             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }