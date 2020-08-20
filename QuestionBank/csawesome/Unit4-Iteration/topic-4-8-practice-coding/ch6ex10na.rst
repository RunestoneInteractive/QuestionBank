.. activecode::  ch6ex10na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :optional:

   public class Test1
   {
       public static void main(String[] args)
       {
           for (int x = 10; x >= 1; x--)
           {
               if (x % 2 == 0)
                   System.out.println(x + " is even");
               else
                   System.out.println(x + " is odd");
           }
       }
   }