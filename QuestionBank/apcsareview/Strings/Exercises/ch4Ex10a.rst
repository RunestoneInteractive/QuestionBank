.. activecode::  ch4Ex10a
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
           String name1 = "ALEX";
           String nameLower= name1.toLowerCase();
           String finalName = name1.substring(0,1) +
                              nameLower.substring(1);
           System.out.println(finalName);
       }
   }