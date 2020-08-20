.. activecode::  ch3Ex8a
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
           int secondsInMinute = 60;
           int minutesInHour = 60;
           int hoursInDay = 24;
           int secondsInDay = secondsInMinute * minutesInHour * hoursInDay;
           int secondsInThreeDays = secondsInDay * 3;
           System.out.println(secondsInThreeDays);
       }
   }