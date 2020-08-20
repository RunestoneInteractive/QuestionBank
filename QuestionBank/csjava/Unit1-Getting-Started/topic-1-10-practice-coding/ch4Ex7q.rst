.. activecode::  ch4Ex7q
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

   Write the code to print "Julian's favorite color is green.  His favorite food is pizza." using the variables provided.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String name = "Julian";
           String color = "green";
           String food = "pizza";
           System.out.println();
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
             String expect = "Julian’s favorite color is green. His favorite food is pizza.";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }