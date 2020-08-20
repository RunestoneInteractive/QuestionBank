.. activecode::  arr2DEx5q
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
   :pct_on_first: 0.6666666667
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.8

   Print the number of rows in the given two-dimensional array, or the length of the outer array. Then print the number of columns, or the length of each inner array.
   ~~~~
   public class Test1
   {
   
       public static void main(String[] args)
       {
           String[][] arr = { {"hello","there","world"},
                             {"how","are","you"} };
   
           System.out.print("Rows:");
           // ADD CODE TO PRINT NUMBER OF ROWS HERE using arr //
   
           System.out.print("Columns:");
           // ADD CODE TO PRINT NUMBER OF COLUMNS HERE using arr //
   
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
            String expect = "Rows:2\nColumns:3";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void test2()
        {
            String target = "arr.length";
            boolean passed = checkCodeContains("using arr and length to get number of rows", target);
           assertTrue(passed);
        }
        @Test
        public void test3()
        {
            String target = "arr[0].length";
            boolean passed = checkCodeContains("using arr[0] and length to get number of columns", target);
           assertTrue(passed);
        }
    }