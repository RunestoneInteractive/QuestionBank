.. activecode::  ch5Ex10a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           double score = 67;
           if (score >= 92)
               System.out.println("A");
           else if (score >= 82)
               System.out.println("B");
           else if (score >= 72)
               System.out.println("C");
           else if (score >= 62)
               System.out.println("D");
           else
               System.out.println("E");

       }
   }