.. activecode::  ch3Ex2q
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
   :pct_on_first: 0.9238095238
   :total_students_attempting: 315
   :num_students_correct: 313.0
   :mean_clicks_to_correct: 1.1214057508

   The following code should calculate the body mass index (BMI) for someone who is 5 feet tall and weighs 110 pounds.  However, the code has syntax errors, like missing semicolons, wrong case on names, or unmatched ``"`` or ``(``. Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           double Height = 60;    // in inches (60 inches is 5 feet)
           double weight  110;    // in pounds
           double heightSquared = height  height;
           double bodyMassIndex = weight / heightSquared
           double bodyMassIndexMetric = bodyMassIndex * 703;
           System.out.println(bodyMassIndexMetric);
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
             String expect = "21.480555555555554\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }