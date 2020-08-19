.. activecode::  ch8Ex4q
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
   :pct_on_first: 0.1428571429
   :total_students_attempting: 7
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 2.3333333333

   Fix the following method ``printEvenElements`` so that it will print out all of the even Integers that are in the passed-in ArrayList ``list``.
   ~~~~
   import java.util.*;
   
   public class Test1
   {
       public static void printEvenElements(ArrayList<Integer> list)
       {
           for (int i = 0; i < list.length; i++)
           {
               if (list.get(i) % 2 == 0)
               {
                   System.out.print(list.get(i) + ", ");
               }
           }
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 44, 7, 9, -16, 3, 2};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           System.out.println("Expected Result:\t 44, -16, 2,");
           System.out.print("Your Result:\t\t ");
           printEvenElements(values);
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
         String expect = "Expected Result:\t44, -16, 2,\n"  +
                         "Your Result:\t\t44, -16, 2,\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testSizeMethod()
       {
         String target = "i < list.size()";
         boolean passed = checkCodeContains("SIZE method used in traversing ArrayList list",target);
         assertTrue(passed);
       }
   
   
     @Test
       public void testIntCast()
       {
         String target = "(int) list.get(i)";
         boolean passed = checkCodeContains("INT CASTING: getting ArrayList list values of type INTEGER ",target);
         assertTrue(passed);
       }
     }