.. activecode::  ch3Ex1q
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
           int tripMiles = 300
           Double price = 2.50;
           int milesPerGallon = 36;
           double numberOfGallons = tripmiles / milesPerGallon;
           double totalCost = numberOfGallons * price;
           System.out.println(totalCost);
       }
   }