.. activecode:: lcdmtest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cDeMorgans
   :topics: Conditionals/cDeMorgans
   :from_source: T
   :language: java

   public class Test1
   {
      public static void main(String[] args)
      {
        int x = 2;
        int y = 3;
        System.out.println(!(x < 3 && y > 2));
      }
   }