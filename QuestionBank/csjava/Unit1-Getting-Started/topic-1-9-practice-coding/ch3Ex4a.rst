.. activecode::  ch3Ex4a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit1-Getting-Started/topic-1-9-practice-coding
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           double originalPrice = 68.00;
           double clearancePrice = originalPrice * 0.3;
           double finalPrice = clearancePrice * 0.8;
           System.out.println(finalPrice);
       }
   }