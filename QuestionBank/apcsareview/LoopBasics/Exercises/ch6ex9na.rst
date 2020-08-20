.. activecode::  ch6ex9na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: Exercises
   :topics: LoopBasics/Exercises
   :from_source: T
   :language: java

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