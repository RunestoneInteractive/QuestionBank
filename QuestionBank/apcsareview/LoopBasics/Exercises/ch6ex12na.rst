.. activecode::  ch6ex12na
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
           String message = "Ix lovex youxxx";
           int pos = message.indexOf("x");
           while (pos >= 0)
           {
              System.out.println(message);
              message = message.substring(0,pos) + message.substring(pos+1);
              pos = message.indexOf("x");
           }
       }
   }