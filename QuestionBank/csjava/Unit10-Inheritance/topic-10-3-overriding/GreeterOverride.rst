.. activecode:: GreeterOverride
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: topic-10-3-overriding
   :topics: Unit10-Inheritance/topic-10-3-overriding
   :from_source: T
   :language: java

   After running the code, try overriding the greet(String) method in the MeanGreeter class to return "Go away" + the who String.
   ~~~~
   public class Greeter
   {
      public String greet()
      {
         return "Hi";
      }

      public String greet(String who)
      {
         return "Hello " + who;
      }

      public static void main(String[] args)
      {
         Greeter g1 = new Greeter();
         System.out.println(g1.greet("Sam"));
         Greeter g2 = new MeanGreeter();
         System.out.println(g2.greet("Nimish"));
      }
   }

   class MeanGreeter extends Greeter
   {
      public String greet()
      {
         return "Go Away";
      }
   }