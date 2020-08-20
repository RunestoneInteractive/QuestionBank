.. activecode::  ch3Ex6a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-10-practice-coding
   :topics: Unit1-Getting-Started/topic-1-10-practice-coding
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
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