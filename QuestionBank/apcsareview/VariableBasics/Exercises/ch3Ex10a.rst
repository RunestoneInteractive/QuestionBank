.. activecode::  ch3Ex10a
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
           double money = 4.5;
           double pricePer = 0.75;
           int num = (int) (money / pricePer);
           System.out.println(num);
       }
   }