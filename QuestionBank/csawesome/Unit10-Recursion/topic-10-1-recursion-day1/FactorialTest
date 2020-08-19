.. activecode:: FactorialTest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: topic-10-1-recursion-day1
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   Run the code below to test the factorial method. What's the factorial of 6? Add another test to print out the factorial of 6. What's the factorial of 1? Add another test to print out the factorial of 1.
   ~~~~
   public class FactorialTest
   {
   
       public static int factorial(int n)
       {
           if (n == 0)
               return 1;
           else
               return n * factorial(n-1);
       }
   
       public static void main(String[] args)
       {
           System.out.println("factorial of 3 is: " + factorial(3));
           System.out.println("factorial of 4 is: " +factorial(4));
           System.out.println("factorial of 5 is: " +factorial(5));
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
             String expect = "factorial of 3 is: 6\nfactorial of 4 is: 24\nfactorial of 5 is: 120\nfactorial of 6 is: 720\nfactorial of 1 is: 1\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }