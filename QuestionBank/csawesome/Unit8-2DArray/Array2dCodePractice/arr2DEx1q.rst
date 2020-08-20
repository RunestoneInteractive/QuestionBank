.. activecode::  arr2DEx1q
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
   :pct_on_first: 0.7419354839
   :total_students_attempting: 31
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.3333333333

   Replace the "ADD CODE HERE" below with the code to declare and create a 3 by 3 two-dimensional int array named ``table``. The finished code will print the values 0 to 8.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           // ADD CODE HERE //
   
           // Should print the values in table
           int count = 0;
           for (int row = 0; row < table.length; row++)
           {
               for (int col = 0; col < table.length; col++)
               {
                   table[row][col] = count;
                   count++;
                   System.out.print(table[row][col] + " ");
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
            String expect = "0 1 2 3 4 5 6 7 8";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void testContains()
        {
            String target = "int[][] table = new int[3][3];";
            boolean passed = checkCodeContains("3x3 declaration of int array table", target);
           assertTrue(passed);
        }
    }