.. activecode::  ch7Ex2q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: ArrayPractice
   :topics: Unit6-Arrays/ArrayPractice
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.7777777778
   :total_students_attempting: 18
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.3888888889

   Fix the following to print the values in the array ``a1`` starting with the value at the last index and then backwards to the value at the first index.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[] a1 = {1, 3, 7, 9, 15};
           for (int i = a1.length; i > 0; i--)
               System.out.print(arr[i] + ", ");
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
             String expect = "15, 9, 7, 3, 1, ";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
         @Test
         public void testCodeContains1(){
           boolean passed = checkCodeContains("correct starting index", "int i = a1.length-1;");
           assertTrue(passed);
         }
   
          @Test
         public void testCodeContains2(){
           boolean passed = checkCodeContains("correct ending index", "i >= 0;");
           assertTrue(passed);
         }
   
          @Test
         public void testCodeContains3(){
           boolean passed = checkCodeContains("correct array variable name", "System.out.print(a1[i] + \", \");");
           assertTrue(passed);
         }
     }