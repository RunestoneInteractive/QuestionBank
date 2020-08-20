.. activecode::  ch7Ex3q
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/ArrayPractice
   :from_source: T
   :language: java

   Rewrite the following code so that it prints all the values in an array ``arr1`` using a for-each loop instead of a ``for`` loop.
   ~~~~
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