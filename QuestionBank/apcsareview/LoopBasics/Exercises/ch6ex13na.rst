.. activecode::  ch6ex13na
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
           for (int x = 5; x >= 1; x--)
           {
              for (int y = x; y > 0; y--)
              {
                  System.out.print(x);
              }
              System.out.println();
           }
       }
   }