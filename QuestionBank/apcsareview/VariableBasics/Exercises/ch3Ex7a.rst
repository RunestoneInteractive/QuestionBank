.. activecode::  ch3Ex7a
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
           double numGallons = 10.0 / 4;
           double milesPerGallon = 32;
           double miles = numGallons * milesPerGallon;
           System.out.println(miles);

       }
   }