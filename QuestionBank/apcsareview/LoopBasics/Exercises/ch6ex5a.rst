.. activecode::  ch6ex5a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: Exercises
   :topics: LoopBasics/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           int x = 1;
           while (x <= 10)
           {
               System.out.println(x);
               x++;
           }
       }
   }