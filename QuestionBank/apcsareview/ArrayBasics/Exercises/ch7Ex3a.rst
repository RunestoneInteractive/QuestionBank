.. activecode::  ch7Ex3a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: Exercises
   :topics: ArrayBasics/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           int[] arr1 = {1, 3, 7, 9};
           for (int value: arr1)
           {
               System.out.print(value + ", ");
           }
       }
   }