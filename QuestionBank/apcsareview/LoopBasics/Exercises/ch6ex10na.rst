.. activecode::  ch6ex10na
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
           for (int x = 10; x >= 1; x--)
           {
               if (x % 2 == 0)
                   System.out.println(x + " is even");
               else
                   System.out.println(x + " is odd");
           }
       }
   }