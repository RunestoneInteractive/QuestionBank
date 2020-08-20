.. activecode::  ch6ex1q
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
           int x = 5;
           while (x > 0)
           {
               System.out.println(x);
               x = x - 1;
           }
       }
   }