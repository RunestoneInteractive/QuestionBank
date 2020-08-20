.. activecode::  ch4Ex5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-9-practice-coding
   :topics: Unit1-Getting-Started/topic-1-9-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.4949494949
   :total_students_attempting: 396
   :num_students_correct: 379.0
   :mean_clicks_to_correct: 1.8311345646

   The following code should print ``Your name is Carly and your favorite color is red``.  Finish the code so that it prints the output correctly using the variables provided.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String name = "Carly";
           String color = "red";
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
             String expect = "Your name is Carly and your favorite color is red";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }