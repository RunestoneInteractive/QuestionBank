.. activecode:: GreeterEx
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :language: java

   Add another subclass called SpanishGreeter (or another language that you know) that extends Greeter and override the greet() method to return "Hola!" (or hi in another language) instead of "Hi!". Create an object to test it out.
   ~~~~
   public class Greeter
   {
      public String greet()
      {
         return "Hi";
      }

      public static void main(String[] args)
      {
         Greeter g1 = new Greeter();
         System.out.println(g1.greet());
         Greeter g2 = new MeanGreeter();
         System.out.println(g2.greet());
      }
   }

   class MeanGreeter extends Greeter
   {
      public String greet()
      {
         return "Go Away";
      }
   }