.. parsonsprob:: ch12p2ex4muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit11-Recursion
   :subchapter: rMixedUpCodePractice
   :topics: Unit11-Recursion/rMixedUpCodePractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following method should recursively count and return the number of 2's that are present in the number.
   -----
   public int numberOf2s(int n)
   {
   =====
       if(n == 0)
   =====
           return 0;
   =====
       else if(n % 10 == 2)
   =====
           return 1 + numberOf2s(n / 10);
   =====
       else
   =====
           return numberOf2s(n / 10);
   =====
   }
   =====
        return 1 + numberOf2s(n % 10); #distractor