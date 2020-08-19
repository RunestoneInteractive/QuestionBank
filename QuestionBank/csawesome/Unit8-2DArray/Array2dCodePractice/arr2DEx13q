.. activecode::  arr2DEx13q
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
   :pct_on_first: 0.9615384615
   :total_students_attempting: 26
   :num_students_correct: 26.0
   :mean_clicks_to_correct: 1.0384615385

   Given the following array, replace the "ADD CODE HERE" below with 1 line of code to replace the word "purple" with "yellow" using the correct array location.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String[][] arr = { {"red","orange", "purple"}, {"green","blue", "indigo"} };
   
           // ADD CODE HERE //
   
           for (int row = 0; row < arr.length; row++)
           {
               for (int col = 0; col < arr[1].length; col++)
               {
                   System.out.println(arr[row][col]);
               }
           }
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
          String expect = "red\norange\nyellow\ngreen\nblue\nindigo\n";
          boolean passed = getResults(expect, output, "Expected output from main");
           assertTrue(passed);
        }
        @Test
        public void test1() throws IOException
        {
            String expect = "arr[0][2] = \"yellow\"";
            boolean passed = checkCodeContains("replacing correct array element with yellow", expect);
            assertTrue(passed);
        }
    }