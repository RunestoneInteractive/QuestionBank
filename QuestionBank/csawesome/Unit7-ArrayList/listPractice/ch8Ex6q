.. activecode::  ch8Ex6q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.8333333333
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.1666666667

   import java.util.List;
   import java.util.ArrayList;
   
   public class Test1
   {
       public static int sumNegValues(ArrayList<Integer> list)
       {
           //code here
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {-2, 34, -11, 9, -6, 3};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           System.out.println("Expected Result:\t -19");
           System.out.print("Your Result:\t\t ");
           System.out.println(sumNegValues(values));
       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     import java.util.List;
     import java.util.ArrayList;
   
     public class RunestoneTests extends CodeTestHelper
     {
       @Test
       public void testMain() throws IOException
       {
         String output = getMethodOutput("main");
         String expect = "Expected Result:\t\t -19\n" +
                         "Your Result:\t -19\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testSumNegValues()
       {
         ArrayList<Integer> values = new ArrayList<Integer>();
         values.add(2);
         values.add(34);
         values.add(-10);
         values.add(9);
         values.add(-5);
         values.add(3);
   
         String output = String.valueOf(Test1.sumNegValues(values));
         String expect = "-15";
   
         boolean passed = getResults(expect, output, "sumNegValues method test");
         assertTrue(passed);
       }
     }