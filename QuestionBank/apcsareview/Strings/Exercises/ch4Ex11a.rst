.. activecode::  ch4Ex11a
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
           String message = "I am very happy!";
           String target = "very ";
           int pos = message.indexOf(target);
           String newMessage = message.substring(0,pos) +
                               message.substring(pos+target.length());
           System.out.println(newMessage);
       }
   }