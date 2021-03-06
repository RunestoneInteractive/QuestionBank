.. activecode::  ch6ex15nq
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
   :pct_on_first: 0.7333333333
   :total_students_attempting: 45
   :num_students_correct: 34.0
   :mean_clicks_to_correct: 1.0294117647

   Write the code below to print a rectangle of stars (``*``) with 3 rows of stars and 5 stars per row.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
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
             String expect = "*****\n*****\n*****\n";
   
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
         @Test
         public void test2() {
             String code = getCode();
             String target = "for (int * = #; * ? *; *~)";
   
             int num = countOccurencesRegex(code, target);
   
             boolean passed = num == 2;
   
             getResults("2", ""+num, "2 For loops (nested)", passed);
             assertTrue(passed);
         }
     }