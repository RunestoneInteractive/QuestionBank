.. activecode:: GreeterOverride
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooOverrideVsOverload
   :topics: OOBasics/ooOverrideVsOverload
   :from_source: T
   :language: java

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