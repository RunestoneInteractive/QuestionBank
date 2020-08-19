.. activecode:: lca2dloopPart2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day2
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day2
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 50
   :num_students_correct: 50.0
   :mean_clicks_to_correct: 1.0

   Looping through just part of a 2D array. Try the CodeLens button.
   ~~~~
   public class Count
   {
      public static int countValues(int value, int[][] a,
                                 int rowStart, int rowEnd,
                                 int colStart, int colEnd)
      {
         int count = 0;
         for (int row = rowStart; row <= rowEnd; row++)
         {
            for (int col = colStart; col <= colEnd; col++)
            {
               if (a[row][col] == value)
                  count++;
            }
         }
         return count;
      }
   
      public static void main(String[] args)
      {
         int[][] matrix = {  {3,2,3},{4,3,6},{8,9,3},{10,3,3}};
         System.out.println(countValues(3,matrix,0,2,0,2));
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
            String expect = "4";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }