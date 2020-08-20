.. activecode::  ch5Ex2a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
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
           int guess = 7;
           int answer = 9;
           if (guess < answer)
               System.out.println("Your guess is too low");
           else if (guess == answer)
               System.out.println("You are right!");
           else
               System.out.println("Your guess is too high");
       }
   }