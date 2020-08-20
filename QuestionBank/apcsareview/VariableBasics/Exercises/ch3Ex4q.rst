.. activecode::  ch3Ex4q
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
           int originalPrice = 68.00;
           int clearancePrice = originalPrice * 0.3;
           int finalPrice = clearancePrice * 0.8;
           System.out.println(finalPrice);
       }
   }