.. activecode::  ch6ex11na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :optional:

   Answer: Use a ``for`` loop with ``x`` changing from 0 to 10 and print the value of ``x`` and ``10 * x``.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           for (int x = 0; x <= 10; x++)
           {
              System.out.println(x * 10);
           }
       }
   }