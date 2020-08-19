.. activecode::  ch8Ex3q
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
   :pct_on_first: 0.5
   :total_students_attempting: 6
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.6

   Fix the following method ``printEvenIndex`` so that it will print out the Integers at even indices of the passed-in ArrayList ``list``.
   ~~~~
   import java.util.*;
   
   public class Test1
   {
       public static void printEvenIndex(ArrayList<Integer> list)
       {
           for (int i)
           {
               if (i % 2 == 1)
               {
                   System.out.print(list.get(i) + ", ");
               }
           }
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
           System.out.println("Expected Result:\t 1, 7, -2, 2,");
           System.out.print("Your Result:\t\t ");
           printEvenIndex(values);
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
         String expect = "Expected Result:\t1, 7, -2, 2,\n" +
                         "Your Result:\t\t1, 7, -2, 2,\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testFor()
       {
         String target = "for (int i = 0; i < list.size(); i++)";
         boolean passed = checkCodeContains("FOR loop: traversing ArrayList list",target);
         assertTrue(passed);
       }
   
   
     @Test
       public void testEvenIndx()
       {
         String target = "if (i % 2 == 0)";
         boolean passed = checkCodeContains("checking EVEN index i: traversing ArrayList list",target);
         assertTrue(passed);
       }
     }