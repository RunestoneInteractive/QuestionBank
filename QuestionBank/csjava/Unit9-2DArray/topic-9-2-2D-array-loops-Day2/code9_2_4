.. activecode:: code9_2_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: topic-9-2-2D-array-loops-Day2
   :topics: Unit9-2DArray/topic-9-2-2D-array-loops-Day2
   :from_source: T
   :language: java

   What will the following code print out? Can you add another method that gets the total for a column?
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

      public static void main(String[] args)
      {
         int[][] matrix = {  {1,2,3},{4,5,6}};
         System.out.println(getTotalForRow(0,matrix));
      }
   }