.. activecode::  ch5Ex9a
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
           int temp = 100;
           if (temp < 30)
               System.out.println("It is freezing");
           else if (temp < 50)
               System.out.println("It is cold");
           else if (temp < 90)
               System.out.println("It is nice out");
           else
               System.out.println("It is hot");
       }
   }