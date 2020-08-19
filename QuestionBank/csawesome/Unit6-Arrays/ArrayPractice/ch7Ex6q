.. activecode::  ch7Ex6q
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
   :pct_on_first: 0.9444444444
   :total_students_attempting: 18
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.2777777778

   Finish the following method to return the sum of all of the non-negative values in the passed array.
   ~~~~
   public class Test1
   {
   
       public static int getSumNonNeg(int[] arr)
       {
       }
   
       public static void main(String[] args)
       {
           int[] a1 = {1, 2, 5, 3, -1, -20};
           System.out.println("The code should print 11 " +
                              "and your answer is: " + getSumNonNeg(a1));
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
             String expect = "The code should print 11 and your answer is: 11";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
         @Test
         public void testMethod(){
            int[] nums = {10, -20, 30, -40, 50};
            Object[] args = {nums};
   
            // name of method, arguments are (nums, 30)
            String output = getMethodOutput("getSumNonNeg", args);
            String expect = "90";
   
            boolean passed = getResults(expect, output,
                     "getSum({10, -20, 30, -40, 50})");
            assertTrue(passed);
         }
     }