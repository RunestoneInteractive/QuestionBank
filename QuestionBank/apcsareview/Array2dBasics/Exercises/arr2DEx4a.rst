.. activecode::  arr2DEx4a
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
           int[][] arr = { {10,39,8},{3},{35,87},{22},{34} };

           // Prints 8, 3, 87, and 34 in order
           System.out.println(arr[0][2]);
           System.out.println(arr[1][0]);
           System.out.println(arr[2][1]);
           System.out.println(arr[4][0]);

       }
   }