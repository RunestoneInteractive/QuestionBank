.. activecode:: ooEx3q
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   public class Dog
   {
       public void speak()
       {
           System.out.println("woof!");
       }

       public static void main(String[] args)
       {
           Dog d = new Dog();
           d.speak();
           Dog b = new Beagle();
           b.speak();
       }
   }

   class Beagle
   {
       public void speak()
       {
           System.out.println("arf arf");
       }
   }