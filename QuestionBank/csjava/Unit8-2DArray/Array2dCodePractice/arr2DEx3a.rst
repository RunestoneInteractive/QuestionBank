.. activecode::  arr2DEx3a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] arr = { {47,3,12},{51,74,20} };

           // Prints 47, 51, 20 in that order
           System.out.println(arr[0][0]);
           System.out.println(arr[1][0]);
           System.out.println(arr[1][2]);
       }
   }