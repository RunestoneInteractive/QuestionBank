.. activecode::  ch6ex1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: Exercises
   :topics: LoopBasics/Exercises
   :from_source: T
   :language: java

   public class Test
   {
       public static void main(String[] args)
       {
           for (int x = 5; x > 0; x = x - 1)
               System.out.println(x);
       }
   }