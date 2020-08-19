.. activecode::  ch7Ex8nq
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
   :pct_on_first: 0.9444444444
   :total_students_attempting: 18
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 1.0555555556

   Finish the method ``getSumChars`` below to return the total number of characters in the array of strings ``strArr``.
   ~~~~
   public class Test1
   {
   
       public static int getSumChars(String[] strArr)
       {
       }
   
       public static void main(String[] args)
       {
           String[] strArr = {"hi", "bye", "hola"};
           System.out.println(getSumChars(strArr));
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
             String expect = "9";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
         @Test
         public void testCodeContains1(){
           boolean passed = checkCodeContains("adding length of each string", ".length()");
           assertTrue(passed);
         }
   
         @Test
         public void testCodecontains(){
           boolean passed = checkCodeContains("for loop", "for");
           assertTrue(passed);
         }
   
         @Test
         public void testMethod(){
            String[] strs = {"a","aa","aaa"};
            Object[] args = {strs};
   
            // name of method, arguments are (nums, 30)
            String output = getMethodOutput("getSumChars", args);
            String expect = "6";
   
            boolean passed = getResults(expect, output,
                     "getSumChars({\"a\",\"aa\",\"aaa\"})");
            assertTrue(passed);
         }
     }