.. activecode:: lccb2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cbasics
   :topics: Conditionals/cbasics
   :from_source: T
   :language: java

   public class Test2
   {
      public static void main(String[] args)
      {
        boolean isHeads = true;
        if (isHeads) System.out.println("Let's go to the game");
        else System.out.println("Let's watch a movie");
        System.out.println("after conditional");
      }
   }