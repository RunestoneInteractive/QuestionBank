.. activecode::  ch4Ex12a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: T
   :language: java

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