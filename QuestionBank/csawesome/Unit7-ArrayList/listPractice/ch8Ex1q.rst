.. activecode::  ch8Ex1q
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
   :pct_on_first: 0.3333333333
   :total_students_attempting: 9
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 2.125

   Fix the following code so that it compiles. The code should instantiate an ArrayList of Strings ``names`` and fill it with the Strings from the array ``friends``. It should then print out ``names``.
   ~~~~
   import java.util.*;
   
   public class Test1
   {
       public static void main(String[] args)
       {
           ArrayList<String> names = new ArrayList<String>();
           String[] friends = {"Sam", "Jessica", "Mark", "Alexis"};
           for (int i = 0; i <= friends.length; i++)
           {
               names.add(friends[i]);
           }
           System.out.println(names);
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
             String expect = "Sam\nJessica\nMark\nAlexis";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }