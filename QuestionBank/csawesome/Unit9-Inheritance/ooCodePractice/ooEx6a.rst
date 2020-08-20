.. activecode::  ooEx6a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :optional:

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