.. activecode:: cs925_whileloopsHW_2
   :author: Doug Vermes
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: Exercises
   :topics: LoopBasics/Exercises
   :from_source: F
   :language: java
   :above:

   Recall that 1 + 3 + 5 + ...+ (2p −1) = p^2 for any integer p≥1. Write a "simple"
   method

      public static boolean isPerfectSquare(int n)

   that tests whether a given number is a perfect square. A "simple" method
   cannot use arrays, nested loops, Math functions, or arithmetic operations
   except addition.
   ~~~~
   public class LoopsHW
   {
      public static boolean isPerfectSquare(int n)
      {
          // IMPLEMENT THIS METHOD

      }

      public static void main(String[] args)
      {
          // DO NOT CHANGE ANYTHING BELOW THIS LINE
          System.out.println("Is " + 9 + " a perfect square? " + isPerfectSquare(9));
          System.out.println("Is " + 11 + " a perfect square? " + isPerfectSquare(11));
          System.out.println("Is " + 49 + " a perfect square? " + isPerfectSquare(49));
      }
   }
   ====