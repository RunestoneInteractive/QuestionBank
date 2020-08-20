.. activecode::  ch7Ex3q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: Exercises
   :topics: ArrayBasics/Exercises
   :from_source: T
   :language: java

   public class Test
   {
       public static void main(String[] args)
       {
           int[] arr1 = {1, 3, 7, 9};
           for (int index = 0; index < arr1.length; index++)
           {
               System.out.print(arr1[index] + ", ");
           }
       }
   }