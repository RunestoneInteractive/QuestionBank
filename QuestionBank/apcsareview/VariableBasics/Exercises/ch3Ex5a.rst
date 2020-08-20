.. activecode::  ch3Ex5a
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
           int numSecs = 320893;
           int numHours = numSecs / 60;
           int numDays = numHours / 24;
           System.out.println(numDays);
        }
   }