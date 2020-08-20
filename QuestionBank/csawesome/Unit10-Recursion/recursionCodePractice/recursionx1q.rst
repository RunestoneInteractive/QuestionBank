.. activecode::  recursionx1q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: recursionCodePractice
   :topics: Unit10-Recursion/recursionCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Replace the "ADD CODE HERE" below with the code to complete the findSum method. The method should take the sum of every value that is less than or equal to n. For example, findSum(3) should return 6. The output of the program should be 15.
   ~~~~
   public class Recursion
   {
       public static int findSum(int n)
       {
           // write code here
       }
   
       public static void main(String[] args)
       {
           System.out.println(findSum(5));
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
            String expect = "15\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }