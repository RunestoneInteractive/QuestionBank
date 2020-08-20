.. activecode::  ooEx10q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: Exercises
   :topics: OOBasics/Exercises
   :from_source: T
   :language: java

   abstract class Animal
   {
       public String name;
       public int numLegs;
       public abstract void speak();
       public abstract void eat();

       public static void main(String[] args)
       {
          Dog myDog = new Dog();
          myDog.speak();
          myDog.eat();
       }
   }

   public class Dog extends Animal
   {
       // ADD CODE HERE

       public static void main(String[] args)
       {
           Dog myDog = new Dog();
           myDog.speak();
           myDog.eat();
       }
   }