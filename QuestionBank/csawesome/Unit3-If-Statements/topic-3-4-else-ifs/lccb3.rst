.. activecode:: lccb3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-4-else-ifs
   :topics: Unit3-If-Statements/topic-3-4-else-ifs
   :from_source: F
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