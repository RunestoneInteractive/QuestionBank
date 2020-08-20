.. activecode::  recursionx1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: recursionCodePractice
   :topics: Unit10-Recursion/recursionCodePractice
   :from_source: T
   :language: java
   :optional:

   public class Recursion
   {
       public static int findSum(int n)
       {
           if (n == 0)
               return 0;
           else
               return n + findSum(n - 1);
       }

       public static void main(String[] args)
       {
           System.out.println(findSum(5));
       }
   }