.. activecode::  ch3Ex3a
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
           double gallonPrice = 2.35;
           double milesPerGallon = 40;
           double totalFunds = 8.0;
           double numGallons = totalFunds / gallonPrice;
           double distance = numGallons * milesPerGallon;
           System.out.println(distance);
       }
   }