.. activecode::  ch3Ex4a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: Exercises
   :topics: VariableBasics/Exercises
   :from_source: T
   :language: java

   public class Test1
   {
       public static void main(String[] args)
       {
           double originalPrice = 68.00;
           double clearancePrice = originalPrice * 0.3;
           double finalPrice = clearancePrice * 0.8;
           System.out.println(finalPrice);
       }
   }