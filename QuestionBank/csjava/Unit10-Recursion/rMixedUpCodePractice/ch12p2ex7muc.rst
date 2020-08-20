.. parsonsprob:: ch12p2ex7muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rMixedUpCodePractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following method should recursively find and print the factorial of int n. It has 1 extra block of code.
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