.. activecode::  arr2DEx12a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: Exercises
   :topics: Array2dBasics/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] arr = { {1,2,3}, {4,5,6}, {7,8,9} };
           for (int row = 0; row < arr.length; row++)
           {
               for (int col = 0; col < arr[1].length; col++)
               {
                   System.out.println(arr[row][col]);
               }
           }
       }
   }