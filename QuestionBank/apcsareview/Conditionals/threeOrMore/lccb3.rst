.. activecode:: lccb3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: threeOrMore
   :topics: Conditionals/threeOrMore
   :from_source: T
   :language: java

   public class Test3
   {
      public static void main(String[] args)
      {
        int x = 2;
        if (x < 0) System.out.println("x is negative");
        else if (x == 0) System.out.println("x is 0");
        else System.out.println("x is positive");
        System.out.println("after conditional");
      }
   }