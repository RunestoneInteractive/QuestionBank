.. activecode::  ooEx12q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: Exercises
   :topics: OOBasics/Exercises
   :from_source: T
   :language: java

   public class Person
   {
       public void speak()
       {
           System.out.println("I'm a person");
       }

       public static void main(String[] args)
       {
           Person p1 = new Student();
           p1.speak();
       }
   }

   class Student extends Person
   {
       // ADD CODE HERE
   }