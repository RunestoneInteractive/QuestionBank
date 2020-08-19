.. activecode::  ch4Ex6q
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
   :pct_on_first: 0.7232375979
   :total_students_attempting: 383
   :num_students_correct: 371.0
   :mean_clicks_to_correct: 1.2991913747

   public class Test1
   {
       public static void main(String[] args)
       {
           String name = "Justin";
           int age = 16;
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
             String expect = "Your name is Justin and your age is 16";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }