.. activecode::  ch7Ex1q
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
           int arr1 = {1, 3, 7, 9, 15, 17};
           for (int index = 0; index <= arr1.length; index+=2)
           {
               System.out.print(index + ", ");
           }
       }
   }