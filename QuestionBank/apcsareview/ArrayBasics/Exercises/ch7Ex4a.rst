.. activecode::  ch7Ex4a
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
           int[] a1 = {0, 3, 6, 7, 9, 10};
           for (int value : a1)
           {
               if (value % 2 == 1)
               {
                   System.out.print(value + " ");
               }
           }
       }
   }