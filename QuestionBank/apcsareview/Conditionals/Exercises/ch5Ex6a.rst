.. activecode::  ch5Ex6a
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
           boolean canWalk = true;
           boolean haveRide = false;
           if (canWalk || haveRide)
               System.out.println("You can go out");
           else
               System.out.println("You can't go out");
       }
   }