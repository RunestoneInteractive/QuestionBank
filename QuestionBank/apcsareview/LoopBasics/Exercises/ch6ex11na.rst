.. activecode::  ch6ex11na
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
           for (int x = 0; x <= 10; x++)
              System.out.println(x + " times 10 is " + (x * 10));
       }
   }