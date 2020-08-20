.. activecode::  JP_ch3Ex9a
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: F
   :language: java

   Write the code to print a random integer number from 100 up to but not including 500.  
   Use ``Math.random()`` to solve this problem.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
          int num = (int) (Math.random()*400) + 100;
          System.out.print(num);
       }
   }