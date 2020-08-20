.. activecode:: ColumnMajorTraversal
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day1
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day1
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 87
   :num_students_correct: 87.0
   :mean_clicks_to_correct: 1.0

   What will the following code print out? Try to guess before you run it. Then, step through it with the CodeLens button.
   ~~~~
   public class ColumnMajorTraversal
   {
     public static void main(String[] args)
      {
        int[][] array = { {1,2,3},{4,5,6}};
        for (int col = 0; col < array[0].length; col++)
        {
            for (int row = 0; row < array.length; row++)
            {
                System.out.println( array[row][col] );
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
        public void test1()
        {
            String output = getMethodOutput("main");
            String expected = "1\n4\n2\n5\n3\n6";
   
            boolean passed = getResults(expected, output, "main()", true);
            assertTrue(passed);
        }
    }