.. activecode::  ch7Ex1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: ArrayPractice
   :topics: Unit6-Arrays/ArrayPractice
   :from_source: T
   :language: java
   :optional:

   Solution to question above.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[] arr1 = {1, 3, 7, 9, 15, 17};
           for (int index = 0; index < arr1.length; index+=2)
           {
               System.out.print(arr1[index] + ", ");
           }
       }
   }