.. activecode::  ch5Ex5a
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
           int x = -3;
           if (x < 0)
               System.out.println("x is less than 0");
           else if (x == 0)
               System.out.println("x is equal to 0");
           else
               System.out.println("x is greater than 0");

       }

   }