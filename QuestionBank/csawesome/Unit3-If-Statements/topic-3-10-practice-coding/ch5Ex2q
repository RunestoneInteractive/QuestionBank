.. activecode::  ch5Ex2q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-10-practice-coding
   :topics: Unit3-If-Statements/topic-3-10-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 1.0
   :total_students_attempting: 58
   :num_students_correct: 58.0
   :mean_clicks_to_correct: 1.0

   The following code should check your guess against the answer and print that it is too low, correct, or too high.  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int guess = 7;
           int answer = 9;
           if guess < answer)
               System.out.println("Your guess is too low);
           else if (guess = answer)
               System.out.println("You are right!");
           else
               System.println("Your guess is too high");
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
             String expect = "Your guess is too low\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }