.. parsonsprob:: ch12p2ex6muc
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
   :pct_on_first: 0.0476190476
   :total_students_attempting: 315
   :num_students_correct: 268.0
   :mean_clicks_to_correct: 12.4029850746

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