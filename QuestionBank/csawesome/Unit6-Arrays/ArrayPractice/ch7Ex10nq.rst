.. activecode::  ch7Ex10nq
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
   :total_students_attempting: 18
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.0

   Finish the method ``getAverage`` to calculate and return the average of all of the values in the array.
   ~~~~
   public class Test1
   {
   
       public static double getAverage(int[] arr)
       {
       }
   
       public static void main(String[] args)
       {
           int[] arr = {20, 3, 18, 55, 4};
           System.out.println(getAverage(arr));;
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
             String expect = "20.0";
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
            int[] nums = {10, 20, 30, 40, 50};
            Object[] args = {nums};
   
            // name of method, arguments are (nums, 30)
            String output = getMethodOutput("getAverage", args);
            String expect = "30.0";
   
            boolean passed = getResults(expect, output,
                     "getAverage({10, 20, 30, 40, 50})");
            assertTrue(passed);
         }
     }