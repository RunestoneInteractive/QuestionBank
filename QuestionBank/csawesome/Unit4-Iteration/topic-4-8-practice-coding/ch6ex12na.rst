.. activecode::  ch6ex12na
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
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
           String message = "Ix lovex youxxx";
           System.out.println(message);
           int pos = message.indexOf("x");
           while (pos >= 0)
           {
              message = message.substring(0,pos) + message.substring(pos+1);
              pos = message.indexOf("x");
              System.out.println(message);
           }
       }
   }