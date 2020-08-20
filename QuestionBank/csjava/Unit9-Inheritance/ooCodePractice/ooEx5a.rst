.. activecode::  ooEx5a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   public class Candy
   {
       public String taste()
       {
           return "tastes sweet!";
       }

       public static void main(String[] args)
       {
           Candy c1 = new Candy();
           System.out.println(c1.taste());
           Candy c2 = new Chocolate();
           System.out.println(c2.taste());
       }
   }

   class Chocolate extends Candy
   {
       public String taste()
       {
           return ("tastes chocolately");
       }
   }