.. activecode::  ch7Ex5a
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
       public static int getSum(int[] arr)
       {
          int sum = 0;
          for (int value : arr)
          {
              sum = sum + value;
          }
          return sum;
       }

       public static void main(String[] args)
       {
           int[] a1 = {1, 2, 5, 3};
           System.out.println("It should print 11 " +
                              " and your answer is: " + getSum(a1));
       }
   }