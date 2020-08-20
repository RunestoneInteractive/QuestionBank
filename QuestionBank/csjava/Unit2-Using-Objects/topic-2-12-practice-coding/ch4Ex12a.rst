.. activecode::  ch4Ex12a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
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
           String message = "That was great - lol.";
           String target = "lol";
           int pos = message.indexOf(target);
           String newMessage = message.substring(0,pos) +
                               "laugh out loud" +
                               message.substring(pos + target.length());
           System.out.println(newMessage);
       }
   }