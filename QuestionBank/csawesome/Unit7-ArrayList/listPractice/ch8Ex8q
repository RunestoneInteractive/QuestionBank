.. activecode::  ch8Ex8q
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
   :mean_clicks_to_correct: 2.0

   Fill in the method ``shiftLeftOne`` below to shift all of the elements of the passed-in ArrayList ``list`` left by one. The original first element should be wrapped to the back of the list after the shift. Ex: {1, 2, 3, 4} should turn turn into {2, 3, 4, 1}
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   
   public class Test1
   {
       public static void shiftLeftOne(ArrayList<Integer> list)
       {
           //code here
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<Integer> values = new ArrayList<Integer>();
           int[] nums = {1, 2, 3, 4, 5};
           for (int i = 0; i < nums.length; i ++)
           {
               values.add(nums[i]);
           }
           shiftLeftOne(values);
           System.out.println("Expected Result:\t [2, 3, 4, 5, 1]");
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
         String expect = "Expected Result:\t [2, 3, 4, 5, 1]\n" +
                         "Your Result:\t\t [2, 3, 4, 5, 1]\n ";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
       @Test
       public void testShiftLeftOne()
       {
         ArrayList<Integer> mylist1 = new ArrayList<Integer>();
         mylist1.add(2);
         mylist1.add(4);
         mylist1.add(1);
   
         ArrayList<Integer> mylist2 = new ArrayList<Integer>();
         mylist2.add(4);
         mylist2.add(1);
         mylist2.add(2);
         Test1.shiftLeftOne(mylist1);
   
         boolean result = mylist2.equals(mylist1);
   
         boolean passed = getResults("true", ""+result, "shiftLeftOne method test");
         assertTrue(passed);
       }
     }