.. activecode::  ch5Ex9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-10-practice-coding
   :topics: Unit3-If-Statements/topic-3-10-practice-coding
   :from_source: T
   :language: java
   :optional:

   This is the answer to the previous question.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int temp = 100;
           if (temp < 30)
               System.out.println("It is freezing");
           else if (temp < 50)
               System.out.println("It is cold");
           else if (temp < 90)
               System.out.println("It is nice out");
           else
               System.out.println("It is hot");
       }
   }