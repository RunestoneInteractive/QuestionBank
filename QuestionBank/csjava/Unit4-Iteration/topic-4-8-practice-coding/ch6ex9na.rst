.. activecode::  ch6ex9na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :optional:

   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "help";
           while (message.length() > 0)
           {
               System.out.println(message);
               message = message.substring(0,message.length() - 1);
           }
       }
   }