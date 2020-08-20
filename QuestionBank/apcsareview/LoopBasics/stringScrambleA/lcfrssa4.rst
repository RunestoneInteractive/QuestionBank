.. activecode:: lcfrssa4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: stringScrambleA
   :topics: LoopBasics/stringScrambleA
   :from_source: T
   :language: java

   public class Test
   {
      public static void main(String[] args)
      {
         System.out.println("WHOA".substring(0,1)); // get the W
         System.out.println("WHOA".substring(1,2)); // get the H - compare the W and H and do nothing
         System.out.println("WHOA".substring(1,2)); // get the H
         System.out.println("WHOA".substring(2,3)); // get the O - compare the H and O and do nothing
         System.out.println("WHOA".substring(2,3)); // get the O
         System.out.println("WHOA".substring(3,4)); // get the A - compare the O and A and do nothing
      }
   }