.. activecode::  arr2DEx9q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.8571428571
   :total_students_attempting: 28
   :num_students_correct: 28.0
   :mean_clicks_to_correct: 1.1428571429

   Replace the "ADD CODE HERE" below with the code to print out the sum of the numbers in the second row of the "table" array.  It should print 18.
   ~~~~
   public class Test1
   {
   
       public static void main(String[] args)
       {
           int[][] table = { {1,4,9},{11,4,3},{2,2,3} };
   
           //ADD CODE HERE
   
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
            String expect = "18";
             boolean passed = output.contains(expect);
              getResults(expect, output, "Expected output from main", passed);
            assertTrue(passed);
        }
        @Test
        public void test1()
        {
          boolean passed = checkCodeContains("1 for loop", "for");
          assertTrue(passed);
        }
    }