.. activecode::  ooEx10a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :optional:

   class Animal
   {
       public String name;
       public int numLegs;
       public void speak() { System.out.println("sniff");}
       public void eat() { System.out.println("crunch"); }
   }

   public class Dog extends Animal
   {
       public void speak()
       {
           System.out.println("woof");
       }

       public void eat()
       {
           System.out.println("num num");
       }

       public static void main(String[] args)
       {
          Dog myDog = new Dog();
          myDog.speak();
          myDog.eat();
       }
   }