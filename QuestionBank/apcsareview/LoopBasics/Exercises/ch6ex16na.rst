.. activecode::  ch6ex16na
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

           String message = "xyxxzax";
           int pos = message.indexOf("x");
           int count = 0;
           while (pos >= 0)
           {
               count++;
               message = message.substring(pos+1);
               pos = message.indexOf("x");
           }
           System.out.println("There were " + count + " x's");
       }
   }