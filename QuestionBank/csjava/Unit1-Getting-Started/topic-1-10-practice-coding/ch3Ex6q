.. activecode::  ch3Ex6q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-10-practice-coding
   :topics: Unit1-Getting-Started/topic-1-10-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   Complete the code below to calculate and print how many months it will take to save $200 if you earn $20 a week.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
         double goal =
         double weeklyRate =
         double numWeeks =
         double numMonths =
         System.out.println(numMonths);
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
         String expect = "2.5\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }

       @Test
       public void testFormulaNumMonths() throws IOException
       {
         String target = "double numMonths = numWeeks / 4;";
         boolean passed = checkCodeContains("formula for numMonths", target);
         assertTrue(passed);
         }
     }