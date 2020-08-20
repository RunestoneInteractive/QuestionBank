.. activecode::  ooEx12a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooCodePractice
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
       public void speak()
       {
           System.out.println("I'm a student");
       }
   }