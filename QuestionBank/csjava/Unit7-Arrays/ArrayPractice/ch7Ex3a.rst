.. activecode::  ch7Ex3a
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
           int[] arr1 = {1, 3, 7, 9};
           for (int value: arr1)
           {
               System.out.print(value + ", ");
           }
       }
   }