.. activecode:: example_trace_loop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: lWhile
   :topics: LoopBasics/lWhile
   :from_source: T
   :language: java

   public class Test
   {
       public static void main(String[] args)
       {
           int var1 = 3;
           int var2 = 2;

           while ((var2 != 0) && ((var1 / var2) >= 0))
           {
               var1 = var1 + 1;
               var2 = var2 - 1;
           }
       }
   }