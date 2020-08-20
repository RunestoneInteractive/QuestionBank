.. activecode::  ch3Ex6a
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
           double weeklyRate = 20;
           double goal = 200;
           double numWeeks = goal / weeklyRate;
           double numMonths = numWeeks / 4;
           System.out.println(numMonths);
       }
   }