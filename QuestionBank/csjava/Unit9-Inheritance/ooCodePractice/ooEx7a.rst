.. activecode::  ooEx7a
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   public class Pet
   {

       public void brag()
       {
           System.out.println("I have the best pet!");
       }

       public static void main(String[] args)
       {
           Dog d1 = new Dog();
           d1.brag();
       }
   }

   class Dog extends Pet
   {
       public void brag()
       {
           super.brag();
           System.out.println("I have the best dog!");
       }
   }