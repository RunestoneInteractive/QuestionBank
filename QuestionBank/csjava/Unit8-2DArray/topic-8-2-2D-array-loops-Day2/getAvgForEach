.. activecode:: getAvgForEach
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day2
   :from_source: T
   :language: java

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