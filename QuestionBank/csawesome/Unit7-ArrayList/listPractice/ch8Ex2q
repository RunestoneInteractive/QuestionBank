.. activecode::  ch8Ex2q
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
   :pct_on_first: 0.7142857143
   :total_students_attempting: 7
   :num_students_correct: 7.0
   :mean_clicks_to_correct: 1.2857142857

   Fix the following class so that it will compile and the method ``reverse`` will return an ArrayList containing Integers in the reversed order of the ArrayList parameter ``list``. Hint: for this solution, only one line needs to be added to the for-loop inside of the ``reverse`` method.
   ~~~~
   import java.util.*;
   
   public class Test1
   {
       public static ArrayList<Integer> reverse(ArrayList<Integer> list)
       {
           ArrayList<int> reversed = new ArrayList<int>();
           for (Integer element: list)
           {
   
           }
           return reversed;
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 5, 7, 9, -2, 3, 2};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           ArrayList<Integer> result = reverse(values);
           System.out.println("Expected Result:\t [2, 3, -2, 9, 7, 5, 1]");
           System.out.println("Your Result:\t\t " + result);
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
         String expect = "Expected Result:    [2, 3, -2, 9, 7, 5, 1]\n" +
                         "Your Result:                [2, 3, -2, 9, 7, 5, 1]\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testAdd()
       {
         String target = "reversed.add(0,element);";
         boolean passed = checkCodeContains("add method called to add element to the beginning of ArrayList reversed",target);
         assertTrue(passed);
       }
     }