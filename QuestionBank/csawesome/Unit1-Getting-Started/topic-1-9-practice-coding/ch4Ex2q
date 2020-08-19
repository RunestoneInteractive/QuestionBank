.. activecode::  ch4Ex2q
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
   :pct_on_first: 0.9513381995
   :total_students_attempting: 411
   :num_students_correct: 409.0
   :mean_clicks_to_correct: 1.0635696822

   The following code should print "Mary's favorite color is blue".  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String name = Mary";
           String color = "blue"
           System.out.println(Name +
                              "'s favorite color is " + color);
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
             String expect = "Mary's favorite color is blue";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }