.. activecode::  ch4Ex4a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "Meet me by the bridge";
           String part = message.substring(0,3);
           String lower = part.toLowerCase();
           System.out.println(lower);
       }
   }