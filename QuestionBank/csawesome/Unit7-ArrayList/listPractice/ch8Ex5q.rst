.. activecode::  ch8Ex5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6666666667
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.8333333333

   Rewrite the following code so that it fills the ArrayList ``values`` with the elements of the array ``nums`` using a for-each loop instead of a ``for`` loop.
   ~~~~
   import java.util.*;
   
   public class Test1
   {
       public static void main(String[] args)
       {
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 44, 7, 9, -16, 3};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           System.out.println("Expected Result:\t [1, 44, 7, 9, -16, 3]");
           System.out.println("Your Result:\t\t " + values);
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
         String expect = "Expected Result:\t[1, 44, 7, 9, -16, 3]\n" +
                         "Your Result:\t\t[1, 44, 7, 9, -16, 3]\n ";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testForEachLoop()
       {
         String target = "for (int * : nums)";
         boolean passed = checkCodeContainsRegex("For-Each loop in traversing Array nums",target);
         assertTrue(passed);
       }
     }