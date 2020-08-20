.. activecode::  ch4Ex3q
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
   :pct_on_first: 0.9592875318
   :total_students_attempting: 393
   :num_students_correct: 392.0
   :mean_clicks_to_correct: 1.0433673469

   The following code should print "Gabby's favorite sport is soccer".  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String name "Gabby";
           String sport = "soccer;
           System.out.println(Name +
                              "'s favorite sport is "
                              sport);
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
             String expect = "Gabby's favorite sport is soccer";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }