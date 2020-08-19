.. activecode:: linearSearch2DArrays
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day2
   :topics: Unit9-2DArray/topic-8-2-2D-array-loops-Day2
   :from_source: F
   :language: java

   What will the following code print? Can you change the code to work for a String 2D array?
   ~~~~
   public class Search
   {
      public static boolean search(int[][] array, int value)
      {
         boolean found = false;
         for (int row = 0; row < array.length; row++)
         {
            for (int col = 0; col < array[0].length; col++)
            {
               if (array[row][col] == value)
                   found = true;
            }
         }
         return found;
      }

      public static void main(String[] args)
      {
         int[][] matrix = {  {3,2,3},{4,3,6},{8,9,3},{10,3,3}};
         System.out.println(search(matrix,10));
         System.out.println(search(matrix,11));

      }
   }