.. activecode::  arr2DEx4q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6333333333
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.4666666667

   Print the values 8, 3, 87, and 34 by accessing them from the given two-dimensional array.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] arr = { {10,39,8},{3},{35,87},{22},{34} };
   
           // ADD CODE HERE //
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testOutput() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "8\n3\n87\n34";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   
        @Test
        public void testDigitOne() throws IOException
        {
          String target = "arr[0][2]";
          boolean passed = checkCodeContains("Correct accessing of 8", target);
          assertTrue(passed);
        }
        @Test
        public void testDigitTwo() throws IOException
        {
          String target = "arr[1][0]";
          boolean passed = checkCodeContains("Correct accessing of 3", target);
          assertTrue(passed);
        }
        @Test
        public void testDigitThree() throws IOException
        {
          String target = "arr[2][1]";
          boolean passed = checkCodeContains("Correct accessing of 87", target);
          assertTrue(passed);
        }
        @Test
        public void testDigitFour() throws IOException
        {
          String target = "arr[4][0]";
          boolean passed = checkCodeContains("Correct accessing of 34", target);
          assertTrue(passed);
        }
    }