.. activecode:: lcgetAverage
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: a2dLoop
   :topics: Array2dBasics/a2dLoop
   :from_source: T
   :language: java

   public class Test
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
         int[][] matrix = { {1,2,3},{4,5,6} };
         System.out.println(getAverage(matrix));
      }
   }