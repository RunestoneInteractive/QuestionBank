.. activecode::  ch8Ex9q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.6

   Finish the method ``moveSmallest`` so that it finds the smallest value in the passed-in ArrayList ``list`` and moves it to the front of the list.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   
   public class Test1
   {
       public static void moveSmallest(ArrayList<Integer> list)
       {
           int smallestIndex = 0;
           for ()
           {
               if ()
               {
                   smallestIndex = i;
               }
           }
           //move smallest to front
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {3, 11, 54, 7, 1, 22};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           moveSmallest(values);
           System.out.println("Expected Result:\t [1, 3, 11, 54, 7, 22]");
           System.out.println("Your Result:\t\t " + values);
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
         String expect = "Expected Result:\t [1, 3, 11, 54, 7, 22]\n" +
                         "Your Result:\t\t [1, 3, 11, 54, 7, 22]\n ";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
       @Test
       public void testMoveSmallest()
       {
         ArrayList<Integer> mylist1 = new ArrayList<Integer>();
         mylist1.add(11);
         mylist1.add(54);
         mylist1.add(7);
         mylist1.add(3);
         mylist1.add(22);
   
         ArrayList<Integer> mylist2 = new ArrayList<Integer>();
         mylist2.add(3);
         mylist2.add(11);
         mylist2.add(54);
         mylist2.add(7);
         mylist2.add(22);
   
         Test1.moveSmallest(mylist1);
   
         boolean result = mylist2.equals(mylist1);
   
         boolean passed = getResults("true", ""+result, "moveSmallest method test");
         assertTrue(passed);
       }
     }