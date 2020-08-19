.. activecode::  ch8Ex10q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listPractice
   :topics: Unit7-ArrayList/listPractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.0

   Finish the method ``findLongest`` to find and return the longest String in the ArrayList of Strings ``list``.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   
   public class Test1 {
       public static String findLongest(ArrayList<String> list)
       {
           //code here
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<String> values = new ArrayList<String>();
           String[] words = {"singapore", "cattle", "metropolitan", "turnstile"};
           for (int i = 0; i < words.length; i ++)
           {
               values.add(words[i]);
           }
           System.out.println("Expected Result:\t metropolitan");
           System.out.print("Your Result:\t\t ");
           System.out.println(findLongest(values));
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
         String expect = "Expected Result:\t metropolitan\n" +
                         "Your Result:\t\t metropolitan\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
       @Test
       public void testFindLongest()
       {
         ArrayList<String> mylist = new ArrayList<String>();
         mylist.add("longword");
         mylist.add("longerword");
         mylist.add("short");
   
         String output = Test1.findLongest(mylist);
         String expect = "longerword";
   
         boolean passed = getResults(output, expect, "findLongest method test");
         assertTrue(passed);
       }
     }