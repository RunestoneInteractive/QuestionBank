.. activecode::  ch6ex2q
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

   Rewrite the following code to use a ``while`` loop instead of a ``for`` loop to print out the numbers from 1 to 10 (inclusive).
   ~~~~
   public class Test
   {
       public static void main(String[] args)
       {
           for (int x = 1; x <= 10; x++)
               System.out.println(x);
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
             String expect = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n";

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