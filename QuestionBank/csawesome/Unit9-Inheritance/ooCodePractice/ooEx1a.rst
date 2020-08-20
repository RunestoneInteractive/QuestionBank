.. activecode::  ooEx1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :optional:

   public class Test1
   {
       public static void talk()
       {
             System.out.println("hello there!");
       }

       public static void talk(String name)
       {
             System.out.println("Hello " + name);
       }

       public static void main(String[] args)
       {
             talk("Matthew");
       }
   }