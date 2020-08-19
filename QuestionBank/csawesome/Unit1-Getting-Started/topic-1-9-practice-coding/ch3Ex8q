.. activecode::  ch3Ex8q
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
   :pct_on_first: 0.5903225806
   :total_students_attempting: 310
   :num_students_correct: 263.0
   :mean_clicks_to_correct: 1.6007604563

   Write the code to calculate the number of seconds in 3 days.  Remember that there are 60 seconds in a minute and 60 minutes in an hour and 24 hours in a day.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
          // Your code should use the variables
          // secondsInDay and secondsInThreeDays
          // and print out secondsInThreeDays
   
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
         String expect = "259200\n";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void testFormulaMiles() throws IOException
       {
         String target1 = removeSpaces("int secondsInThreeDays = secondsInDay * 3;");
         String target2 = removeSpaces("int secondsInThreeDays = 3 * secondsInDay;");
         String code = removeSpaces(getCode());
         boolean passed1 = code.contains(target1);
         boolean passed2 = code.contains(target2);
   
         boolean passed = passed1 || passed2;
         getResults("true", "" + passed, "formula for secondsInThreeDays using secondsInDay", passed);
         assertTrue(passed);
       }
     }