.. activecode::  ch7Ex2a
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
           int[] a1 = {1, 3, 7, 9, 15};
           for (int i = a1.length - 1; i >= 0; i--)
               System.out.print(a1[i] + ", ");
       }
   }