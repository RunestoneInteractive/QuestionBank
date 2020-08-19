.. activecode:: lcfrgib3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: grayImageB
   :topics: Unit8-2DArray/grayImageB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4
   :total_students_attempting: 5
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Fix the terminating conditions of the loops so that we do not go beyond the array bounds
   ~~~~
   public class LoopTest
   {
      public static void main(String[] args)
      {
        int[][] values = { {9, 8, 7, 6, 5},
                          {7, 6, 5, 4, 3},
                          {4, 3, 2, 1, 0},
                          {4, 3, 2, 1, 0}};
        for (int i = 0; i < values.length; i++)
        {
          for (int j = i; j < values[i].length; j++)
          {
            System.out.print(values[i][j] - values[i+2][j+2]);
          }
          System.out.println();
        }
      }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     import java.util.List;
     import java.util.ArrayList;
     import java.util.Arrays;
   
     public class RunestoneTests extends CodeTestHelper
     {
   
       @Test
       public void testMain() throws IOException
       {
         String output = getMethodOutput("main");
         String expect = "777\n" +
                         "55\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
     }