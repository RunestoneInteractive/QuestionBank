.. activecode::  ch7Ex7nq
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
   :pct_on_first: 0.6315789474
   :total_students_attempting: 19
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.5

   Finish the following code to print the strings at the odd indices in the array.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String[] stArr1 = {"Destini", "Landon", "Anaya", "Gabby", "Evert"};
   
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
             String expectNewL = "Landon\nGabby\n";
             boolean passedNewL = getResults(expectNewL, output, "Expected output from main");
             assertTrue(passedNewL);
         }
         @Test
         public void testCodeContains()
         {
   
             boolean passed = checkCodeContains("for loop", "for");
             assertTrue(passed);
         }
     }