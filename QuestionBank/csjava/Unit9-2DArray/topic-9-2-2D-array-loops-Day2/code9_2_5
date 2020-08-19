.. activecode:: code9_2_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: topic-9-2-2D-array-loops-Day2
   :topics: Unit9-2DArray/topic-9-2-2D-array-loops-Day2
   :from_source: T
   :language: java

   Loooping through just part of a 2D array.
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
               if (a[row][col] == value) count++;
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