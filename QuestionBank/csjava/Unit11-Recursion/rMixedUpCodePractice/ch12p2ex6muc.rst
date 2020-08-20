.. parsonsprob:: ch12p2ex6muc
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

   The following method should recursively find and return the number of even digits in int n.
   -----
   public int evenDigits(int n)
   {
   =====
       if(n / 10 == 0)
   =====
           if(n % 2 == 0)
   =====
            return 1;
   =====
            else return 0;
   =====
        else if((n % 10) % 2 == 0)
   =====
                return evenDigits(n / 10) + 1;
   =====
                else
   =====
                return evenDigits(n / 10);
   =====
   }