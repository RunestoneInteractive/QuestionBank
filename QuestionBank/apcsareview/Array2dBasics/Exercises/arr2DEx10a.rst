.. activecode::  arr2DEx10a
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
           int[][] array = { {1,2,3},{-1,-2,-3},{4,5,6} };
           int total = 0;

           for (int row = 0; row < array.length; row++)
           {
               total += array[row][row];

           }

           System.out.println("The sum of the diagonal is: "+ total);

       }
   }