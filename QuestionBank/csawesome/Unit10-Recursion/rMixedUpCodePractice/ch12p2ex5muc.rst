.. parsonsprob:: ch12p2ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rMixedUpCodePractice
   :topics: Unit10-Recursion/rMixedUpCodePractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.4875
   :total_students_attempting: 320
   :num_students_correct: 292.0
   :mean_clicks_to_correct: 2.0068493151

   The following method should recursively find and return the sum of the digits of int n.
   -----
   public int sum(int n)
   {
   =====
       if(n / 10 == 0)
   =====
           return n;
   =====
       else
   =====
           return sum(n / 10) + n % 10;
   =====
   }
   =====
        return 1 + sum(n % 10); #distractor