.. parsonsprob:: ch12p2ex7muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rMixedUpCodePractice
   :topics: Recursion/rMixedUpCodePractice
   :from_source: T
   :adaptive:
   :noindent:

   The following method should recursively find and print the factorial of int n.
   -----
   public int factorial(int n)
   {
   =====
       if(n == 1)
   =====
           return 1;
   =====
       else
   =====
           return n * factorial(n - 1);
   =====
   }
   =====
        return 1 + factorial(n % 10); #distractor