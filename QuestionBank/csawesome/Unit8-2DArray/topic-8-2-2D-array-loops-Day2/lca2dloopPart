.. activecode:: lca2dloopPart
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day2
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day2
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4150943396
   :total_students_attempting: 53
   :num_students_correct: 41.0
   :mean_clicks_to_correct: 2.8780487805

   What will the following code print out? Can you complete the  method called ``getTotalForCol`` that gets the total for a column? To do this, you must loop through the rows. The array's length will tell you how many rows you have since it is an array of arrays, while the length of the array's first element will tell you how many columns.
   ~~~~
   public class Total
   {
   
      public static int getTotalForRow(int row, int[][] a)
      {
         int total = 0;
         for (int col = 0; col < a[0].length; col++)
         {
            total = total + a[row][col];
         }
         return total;
      }
   
      // Complete the method getTotalForCol below
      public static int getTotalForCol(int col, int[][] a)
      {
          int total = 0;
          // Add a loop here to total a column col
   
   
          return total;
      }
   
      public static void main(String[] args)
      {
         int[][] matrix = {  {1,2,3},{4,5,6}};
         System.out.println(getTotalForRow(0,matrix));
         System.out.println(getTotalForCol(0,matrix));
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
         public RunestoneTests() {
            super("Total");
        }
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "6\n5";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
            public void test2()
            {
                int[][] array = { {1,4,8},{6,7,9} };
                int value = 0;
                Object[] args = {value, array};
   
   
                String output = getMethodOutput("getTotalForCol", args);
                String expect = "7";
   
                boolean passed = getResults(expect, output, "Testing getTotalForCol(0, { {1, 4,8},{6, 7, 9} })");
                assertTrue(passed);
            }
    }