.. activecode::  ch3Ex3a
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
           double gallonPrice = 2.35;
           double milesPerGallon = 40;
           double totalFunds = 8.0;
           double numGallons = totalFunds / gallonPrice;
           double distance = numGallons * milesPerGallon;
           System.out.println(distance);
       }
   }