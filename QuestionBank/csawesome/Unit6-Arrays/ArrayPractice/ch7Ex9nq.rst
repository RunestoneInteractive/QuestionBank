.. activecode::  ch7Ex9nq
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
   :pct_on_first: 1.0
   :total_students_attempting: 12
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 1.0

   Finish the method ``findMin`` so that it finds and returns the minimum value in the array.
   ~~~~
   public class Test1
   {
   
       public static int findMin(int[] arr)
       {
       }
   
       public static void main(String[] args)
       {
           int[] arr = {20, -3, 18, 55, 4};
           System.out.println(findMin(arr));
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
             String expect = "-3";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
         @Test
         public void testCodeContains2(){
           boolean passed = checkCodeContains("for loop", "for");
           assertTrue(passed);
         }
   
          @Test
         public void testMethod(){
            int[] nums = {10, 20, 5, 40, 50};
            Object[] args = {nums};
   
            // name of method, arguments are (nums, 30)
            String output = getMethodOutput("findMin", args);
            String expect = "5";
   
            boolean passed = getResults(expect, output,
                     "findMin({10, 20, 5, 40, 50})");
            assertTrue(passed);
         }
     }