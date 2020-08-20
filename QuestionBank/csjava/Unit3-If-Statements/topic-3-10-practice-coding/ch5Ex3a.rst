.. activecode::  ch5Ex3a
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
           boolean doneHomework = true;
           boolean cleanedRoom = true;
           if (doneHomework && cleanedRoom)
               System.out.println("You can go out");
           else
               System.out.println("You cannot go out");
       }
   }