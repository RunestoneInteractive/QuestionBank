.. activecode::  ch7Ex6a
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

       public static int getSumNonNeg(int[] arr)
       {
           int sum = 0;
           for (int value : arr)
           {
               if (value >= 0)
                   sum = sum + value;
           }
           return sum;
       }


       public static void main(String[] args)
       {
           int[] a1 = {1, 2, 5, 3, -1, -20,};
           System.out.println("The code should print 11 " +
                              "and your answer is: " + getSumNonNeg(a1));
       }
   }