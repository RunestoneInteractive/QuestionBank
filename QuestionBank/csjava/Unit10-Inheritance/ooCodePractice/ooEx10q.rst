.. activecode::  ooEx10q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit10-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   class Animal
   {
       public String name;
       public int numLegs;
       public void speak() { System.out.println("sniff");}
       public void eat() { System.out.println("crunch"); }

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