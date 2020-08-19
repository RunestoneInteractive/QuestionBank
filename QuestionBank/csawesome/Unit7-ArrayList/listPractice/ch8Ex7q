.. activecode::  ch8Ex7q
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
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.0

   Finish the following method ''removeLongStrings'' that checks each element of the passed in ArrayList ``list`` and removes any that are strictly longer than 4 characters.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   
   public class Test1
   {
       public static void removeLongStrings(ArrayList<String> list)
       {
           //code here
       }
   
       public static void main(String[] args)
       {
           //instantiate ArrayList and fill with Integers
           ArrayList<String> values = new ArrayList<String>();
           String[] words = {"bathtub", "fish", "computer", "cat", "foo"};
           for (int i = 0; i < words.length; i ++)
           {
               values.add(words[i]);
           }
           removeLongStrings(values);
           System.out.println("Expected Result:\t [fish, cat, foo]");
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
         String expect = "Expected Result:\t [fish, cat, foo]\n" +
                         "Your Result:\t\t [fish, cat, foo]\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testRemoveLongStrings()
       {
         ArrayList<String> mylist1 = new ArrayList<String>();
         mylist1.add("longword");
         mylist1.add("dog");
         mylist1.add("longword");
         mylist1.add("wee");
   
         ArrayList<String> mylist2 = new ArrayList<>();
         mylist2.add("dog");
         mylist2.add("wee");
   
         Test1.removeLongStrings(mylist1);
   
         boolean result = mylist2.equals(mylist1);
   
         boolean passed = getResults("true", ""+result, "removeLongStrings method test");
         assertTrue(passed);
       }
     }