.. activecode:: offbyone
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit7-Arrays/topic-6-2-traversing-arrays
   :from_source: F
   :language: java

   The following code has an ArrayIndexOutOfBoundsException. It has 2 common off-by-one errors in the loop. Can you fix it and make the loop print out all the scores?
   ~~~~
   public class OffByone
   {
      public static void main(String[] args)
      {
          int[] scores = { 10, 9, 8, 7};
          // Make this loop print out all the scores!
          for (int i = 1; i <= scores.length; i++)
          {
               System.out.println(  scores[i] );
          }
      }
    }