.. activecode::  ch7Ex6q
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

       public static int getSumNonNeg(int[] arr)
       {
       }

       public static void main(String[] args)
       {
           int[] a1 = {1, 2, 5, 3, -1, -20};
           System.out.println("The code should print 11 " +
                              "and your answer is: " + getSumNonNeg(a1));
       }
   }