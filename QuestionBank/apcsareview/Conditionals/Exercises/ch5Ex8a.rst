.. activecode::  ch5Ex8a
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
           double temp = 103.5;
           if (temp > 100)
               System.out.println("You have a fever");
           else
               System.out.println("You don't have a fever");
       }
   }