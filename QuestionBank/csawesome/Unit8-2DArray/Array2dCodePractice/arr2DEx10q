.. activecode::  arr2DEx10q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.7692307692
   :total_students_attempting: 26
   :num_students_correct: 26.0
   :mean_clicks_to_correct: 1.2692307692

   Replace the "ADD CODE HERE" below with the code to find the sum of the values on the diagonal from [0][0] to [num rows - 1][num rows - 1]. Print the sum.  It should print 5.
   ~~~~
   public class Test1
   {
   
       public static void main(String[] args)
       {
           int[][] array = { {1,2,3},{-1,-2,-3},{4,5,6} };
   
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
            String expect = "5";
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