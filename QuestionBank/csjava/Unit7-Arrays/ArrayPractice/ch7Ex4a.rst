.. activecode::  ch7Ex4a
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