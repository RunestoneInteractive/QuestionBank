.. activecode:: lcgetAverage
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day1
   :topics: Unit9-2DArray/topic-8-2-2D-array-loops-Day1
   :from_source: F
   :language: java
   :autograde: unittest

   What does the following code do? Add another row of numbers to the matrix. Will the loops traverse this row too? Note that an array can be passed in as an argument to a method. Click on the CodeLens button and then next to step through this code in the visualizer.
   ~~~~
   public class Test1
   {

      public static double getAverage(int[][] a)
      {
         double total = 0;
         int value = 0;
         for (int row = 0; row < a.length; row++)
         {
            for (int col = 0; col < a[0].length; col++)
            {
               value = a[row][col];
               total = total + value;
            }
         }
         return total / (a.length * a[0].length);
      }

      public static void main(String[] args)
      {
         int[][] matrix = { {1,2,3},{4,5,6}};
         System.out.println(getAverage(matrix));
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
            String expected = "3.5";

            boolean passed = !output.contains(expected);

            passed = getResults("true", ""+passed, "Average has changed");
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String code = getCode();
            String expected = "int[][] matrix = { {1,2,3},{4,5,6}};";

            boolean passed = !code.replaceAll(" ","").contains(expected.replaceAll(" ",""));

            passed = getResults("true", ""+passed, "Matrix has been changed");
            assertTrue(passed);
        }
    }