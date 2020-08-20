.. activecode:: code9_2_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: topic-9-2-2D-array-loops-Day2
   :topics: Unit9-2DArray/topic-9-2-2D-array-loops-Day2
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