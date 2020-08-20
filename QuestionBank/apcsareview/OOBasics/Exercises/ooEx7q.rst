.. activecode::  ooEx7q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: Exercises
   :topics: OOBasics/Exercises
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
           // ADD CODE HERE

           System.out.println("I have the best dog!");
       }
   }