.. activecode::  ch6ex14na
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
           for (int row = 0; row < 5; row++)
           {
              for (int col = 0; col < 3; col++)
              {
                  System.out.print("*");
              }
              System.out.println();
           }
       }
   }