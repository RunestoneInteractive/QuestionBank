.. activecode::  arr2DEx2q
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
   :pct_on_first: 0.8
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.2333333333

   Replace the "ADD CODE HERE" below with the code to declare and initialize a two-dimensional String array called ``students`` with the names "Brice, Marvin, Anna" in the first row and "Kamal, Maria, Elissa" in the second. The finished code will print all the names in the array starting with all in the first row followed by all in the second row.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           // ADD CODE HERE //
   
   
           // Should print the values in students in order
           for (int row = 0; row < students.length; row++)
           {
               for (int col = 0; col < students[0].length; col++)
               {
                   System.out.print(students[row][col] + " ");
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
            String expect = "Brice Marvin Anna Kamal Maria Elissa";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void testContains()
        {
            String target = "String[][] students";
            boolean passed = checkCodeContains("2D String array called students", target);
           assertTrue(passed);
        }
    }