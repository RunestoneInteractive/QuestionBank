.. activecode::  ch6ex4a
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
           int x = 10;
           while (x <= 100)
           {
               System.out.println(x);
               x = x + 10;
           }
       }
   }