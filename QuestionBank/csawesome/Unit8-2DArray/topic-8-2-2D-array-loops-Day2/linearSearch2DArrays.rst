.. activecode:: linearSearch2DArrays
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day2
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day2
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.387755102
   :total_students_attempting: 49
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 1.5833333333

   What will the following code print? Can you change the code to work for a String 2D array instead of an int array? Note that the indices row and col will still be ints.
   ~~~~
   public class Search
   {
      public static boolean search(int[][] array, int value)
      {
         boolean found = false;
         for (int row = 0; row < array.length; row++)
         {
            for (int col = 0; col < array[0].length; col++)
            {
               if (array[row][col] == value)
                   found = true;
            }
         }
         return found;
      }
   
      public static void main(String[] args)
      {
         int[][] matrix = { {3,2,3},{4,3,6},{8,9,3},{10,3,3} };
         System.out.println(search(matrix,10));
         System.out.println(search(matrix,11));
   
        // Comment out the code above, and try these:
        // String[][] matrix2 = { {"a","b","c"},{"d","e","f"} };
        // System.out.println(search(matrix2, "b"));
   
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Search");
        }
   
        @Test
            public void test2()
            {
                String[][] array = { {"a","b","c"},{"d","e","f"},{"g","h","i"},{"j","k","l"} };
                String value = "b";
                Object[] args = {array, value};
   
   
                String output = getMethodOutput("search", args);
                String expect = "true";
   
                boolean passed = getResults(expect, output, "Testing search({ {\"a\",\"b\",\"c\"},{\"d\",\"e\",\"f\"},{\"g\",\"h\",\"i\"},{\"j\",\"k\",\"l\" } }, \"b\")");
                assertTrue(passed);
            }
    }