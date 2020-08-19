.. activecode::  ch3Ex7q
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
   :pct_on_first: 0.3118971061
   :total_students_attempting: 311
   :num_students_correct: 266.0
   :mean_clicks_to_correct: 2.8947368421

   Write the code to calculate the number of miles you can drive if you have a 10 gallon gas tank and are down to a quarter of a tank of gas and your car gets 32 miles per gallon.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
          // Your code should use the variables
          // numGallons, milesPerGallon, and miles
          // and print out miles
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
         String expect = "80.0\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testFormulaMiles() throws IOException
       {
         String target1 = removeSpaces("double miles = numGallons * milesPerGallon;");
         String target2 = removeSpaces("double miles = milesPerGallon * numGallons;");
         String code = removeSpaces(getCode());
   
         boolean passed1 = code.contains(target1);
         boolean passed2 = code.contains(target2);
   
         boolean passed = passed1 || passed2;
   
         getResults("true", ""+passed, "formula for miles using milesPerGallon and numGallons", passed);
         assertTrue(passed);
       }
     }