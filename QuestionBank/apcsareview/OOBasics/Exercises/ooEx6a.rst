.. activecode::  ooEx6a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: Exercises
   :topics: OOBasics/Exercises
   :from_source: T
   :language: java

   public class Student
   {

       public static void greet()
       {
           System.out.println("Hello");
       }

       public static void greet(String name)
       {
           System.out.println("Hello " + name);
       }

       public static void main(String[] args)
       {
          greet();
          greet("Sansa");
       }
   }