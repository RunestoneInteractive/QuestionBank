.. activecode::  ch6ex8na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
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
           for (int x = 100; x >= 0; x = x - 10)
               System.out.println(x);
       }
   }