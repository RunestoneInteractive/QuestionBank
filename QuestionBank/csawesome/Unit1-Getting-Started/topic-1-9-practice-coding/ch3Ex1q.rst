.. activecode::  ch3Ex1q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-9-practice-coding
   :topics: Unit1-Getting-Started/topic-1-9-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.9742857143
   :total_students_attempting: 350
   :num_students_correct: 350.0
   :mean_clicks_to_correct: 1.0342857143

   The following code should calculate the cost of a trip that is 300 miles if gas is $2.50 a gallon and your car gets 30 miles per gallon.  However, the code has syntax errors, like missing semicolons, wrong case on names, or unmatched ``"`` or ``(``.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int tripMiles = 300
           Double price = 2.50;
           int milesPerGallon = 30;
           double numberOfGallons = tripmiles / milesPerGallon;
           double totalCost = numberOfGallons * price;
           System.out.println(totalCost);
       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testMain() throws IOException
         {
             String output = getMethodOutput("main");
             String expect = "25.0";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }