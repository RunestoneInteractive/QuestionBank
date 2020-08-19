.. activecode::  ch7Ex3q
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
   :pct_on_first: 0.65
   :total_students_attempting: 20
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 1.5294117647

   Rewrite the following code so that it prints all the values in an array ``arr1`` using a for-each loop instead of a ``for`` loop.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[] arr1 = {1, 3, 7, 9};
           for (int index = 0; index < arr1.length; index++)
           {
               System.out.print(arr1[index] + ", ");
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
         public void testCodeContains()
         {
   
             boolean passed = checkCodeContains("for each loop", "for (int * : arr1)");
             assertTrue(passed);
         }
   
         @Test
         public void testCodeContains1()
         {
   
             boolean passed = checkCodeContains("print statement variable name", "System.out.print(* + \", \");");
             assertTrue(passed);
         }
     }