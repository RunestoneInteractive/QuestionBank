.. activecode:: while_loop_ex1
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: lbasics
   :topics: Unit4-Iteration/lbasics
   :from_source: F
   :language: java

   public class Test
   {
      public static void main(String[] args)
      {
          int x = 3;
          while (x > 0)
          {
             System.out.println(x);
             x = x - 1;
          }
      }
   }