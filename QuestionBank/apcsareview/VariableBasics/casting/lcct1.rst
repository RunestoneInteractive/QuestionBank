.. activecode:: lcct1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: casting
   :topics: VariableBasics/casting
   :from_source: T
   :language: java

   public class Test
   {
      public static void main(String[] args)
      {
        System.out.println(1 / 3);
        System.out.println(1.0 / 3);
        System.out.println(1 / 3.0);
        System.out.println((double) 1 / 3);
      }
   }