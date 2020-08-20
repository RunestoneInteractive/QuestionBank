.. activecode::  arr2DEx8a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :optional:

   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] array = { {4,7,8},{8,8,7} };

           int count = 0;

           for (int row = 0; row < array.length; row++)
           {
               for (int col = 0; col < array[0].length; col++)
               {
                   if (array[row][col]==7)
                       count++;
               }

           }

           System.out.println(count);
       }
   }