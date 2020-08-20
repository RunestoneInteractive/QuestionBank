.. activecode::  ch3Ex2a
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
           double height = 60;    // in inches (60 inches is 5 feet)
           double weight = 110;    // in pounds
           double heightSquared = height * height;
           double bodyMassIndex = weight / heightSquared;
           double bodyMassIndexMetric = bodyMassIndex * 703;
           System.out.println(bodyMassIndexMetric);
       }
   }