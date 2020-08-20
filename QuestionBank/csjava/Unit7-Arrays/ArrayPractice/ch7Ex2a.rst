.. activecode::  ch7Ex2a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: ArrayPractice
   :topics: Unit7-Arrays/ArrayPractice
   :from_source: T
   :language: java

   Solution to question above.
   ~~~~
   public class Test
   {
       public static void main(String[] args)
       {
           int[] a1 = {1, 3, 7, 9, 15};
           for (int i = a1.length - 1; i >= 0; i--)
               System.out.print(a1[i] + ", ");
       }
   }