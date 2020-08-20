.. activecode::  arr2DEx7q
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
   :pct_on_first: 0.5517241379
   :total_students_attempting: 29
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 1.6551724138

   Declare and create a two-dimensional array of strings named ``colors``.  Put the colors ("red", "yellow", "blue") in the first row, and the colors ("orange", "green", "purple") in the second row. Then print every value in the array.
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
        public void testArrayDec() throws IOException
        {
            String code = removeSpaces(getCode());
            String expect =removeSpaces("String[][] colors = { {\"red\", \"yellow\", \"blue\"},{\"orange\", \"green\", \"purple\"}}");
   
            boolean passed = code.contains(expect);
            getResults("true", passed+"", "correct initialization of array", passed);
          assertTrue(passed);
        }
        @Test
        public void testOutput() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "red yellow blue \norange green purple";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }