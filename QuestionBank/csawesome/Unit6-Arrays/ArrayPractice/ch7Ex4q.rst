.. activecode::  ch7Ex4q
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
   :pct_on_first: 0.6
   :total_students_attempting: 20
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.6666666667

   Finish the following code so that it prints out all of the odd values in the array ``a1``. Hint: use % to check for odd values.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[] a1 = {0, 3, 6, 7, 9, 10};
           for (int value : a1)
           {
           }
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
             String expect = "3 7 9 ";
   
             boolean passed = getResults(expect, output, "Expected output from main");
              assertTrue(passed);
         }
         @Test
         public void testContains()
         {
           boolean passed = checkCodeContains("Use % to see if value is odd","value % 2 ");
           assertTrue(passed);
         }
     }