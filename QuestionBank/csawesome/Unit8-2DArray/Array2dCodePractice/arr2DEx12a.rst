.. activecode::  arr2DEx12a
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
           int[][] numbers = { {1,2,3}, {4,5,6}, {7,8,9} };
           for (int row = 0; row < numbers.length; row++)
           {
               for (int col = 0; col < numbers[1].length; col++)
               {
                   System.out.println(numbers[row][col]);
               }
           }
       }
   }