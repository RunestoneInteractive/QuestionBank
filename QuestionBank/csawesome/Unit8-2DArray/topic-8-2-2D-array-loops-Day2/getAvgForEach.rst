.. activecode:: getAvgForEach
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
   :total_students_attempting: 56
   :num_students_correct: 56.0
   :mean_clicks_to_correct: 1.0

   Nested enhanced for loops demo. Click on the CodeLens button to visualize and step through the code.
   ~~~~
   public class Average
   {
   
      public static double getAvg(int[][] a)
      {
         double total = 0;
         for (int[] innerArray : a)
         {
            for (int val : innerArray)
            {
               total = total + val;
            }
         }
         return total / (a.length * a[0].length);
      }
   
      public static void main(String[] args)
      {
         int[][] theArray = {  {80, 90, 70}, {20, 80, 75}};
         System.out.println(getAvg(theArray));
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
            String expect = "69.16666666666667";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }