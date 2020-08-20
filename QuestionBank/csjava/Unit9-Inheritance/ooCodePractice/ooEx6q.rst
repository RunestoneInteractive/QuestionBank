.. activecode::  ooEx6q
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   public class Student
   {
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