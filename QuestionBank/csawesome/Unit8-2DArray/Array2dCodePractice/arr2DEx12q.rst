.. activecode::  arr2DEx12q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.8846153846
   :total_students_attempting: 26
   :num_students_correct: 26.0
   :mean_clicks_to_correct: 1.2307692308

   Replace the "ADD CODE HERE" below with the code to declare and create a two-dimensional array of integers ``numbers`` with the numbers (1,2,3) in the first row, the numbers (4,5,6) in the second row, and the numbers (7,8,9) in the third row. Then loop through the two-dimensional array, printing out the values in the first row followed by those in the second row and so on.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
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
        public void testMain() throws IOException
        {
          String output = getMethodOutput("main");
          String expect = "1 2 3\n4 5 6\n7 8 9";
          boolean passed = getResults(expect, output, "Expected output from main");
           assertTrue(passed);
        }
        @Test
        public void test1()
        {
          String expect = "int[][] numbers = { {1,2,3},{4,5,6}, {7,8,9}}";
          boolean passed = checkCodeContains("correct array initialization", expect);
          assertTrue(passed);
        }
           @Test
        public void test2()
        {
            String target = "for";
            int num = countOccurences(getCode(), target);
            boolean passed = (num == 2);
            getResults("2", num+"","2 for loops",passed);
            assertTrue(passed);
        }
   
    }