.. activecode::  ooEx5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: Exercises
   :topics: OOBasics/Exercises
   :from_source: T
   :language: java

   public class Candy
   {
       public String taste()
       {
           return "tastes sweet!"
       }

       public static void main(String[] args)
       {
           Candy c1 = new Candy();
           System.out.println(c1.taste());
           Candy c2 = new Chocolate();
           System.out.println(c2.taste();
       }
   }

   class Chocolate extends Candy
   {
       // ADD CODE HERE
   }