.. activecode::  ch6ex3q
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

   Rewrite the following code so that it uses a ``for`` loop instead of a ``while`` loop to print out all the integers from 5 to 15 (inclusive).
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 5;
           while (x <= 15)
           {
               System.out.println(x);
               x = x + 1;
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
             String expect = "5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n";

             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }

         @Test
         public void testForLoop() throws IOException
         {
             String target = "for (int x = 5;";
             boolean passed = checkCodeContains("for loop", target);
             assertTrue(passed);
         }
     }