.. activecode:: lca2dloopPart
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: a2dLoopPart
   :topics: Array2dBasics/a2dLoopPart
   :from_source: T
   :language: java


   public class Test
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
         int[][] matrix = { {1,2,3},{4,5,6} };
         System.out.println(getTotalForRow(0,matrix));
      }
   }