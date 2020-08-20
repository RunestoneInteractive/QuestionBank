.. activecode::  ch7Ex5a
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