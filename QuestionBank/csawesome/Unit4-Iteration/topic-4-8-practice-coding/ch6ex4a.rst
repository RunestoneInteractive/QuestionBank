.. activecode::  ch6ex4a
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
           int x = 10;
           while (x <= 100)
           {
               System.out.println(x);
               x = x + 10;
           }
       }
   }