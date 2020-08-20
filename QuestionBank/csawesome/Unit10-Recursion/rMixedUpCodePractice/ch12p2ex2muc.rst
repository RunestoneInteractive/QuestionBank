.. parsonsprob:: ch12p2ex2muc
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
   :pct_on_first: 0.5045317221
   :total_students_attempting: 331
   :num_students_correct: 304.0
   :mean_clicks_to_correct: 3.1118421053

   The following method should recursively return the fibonacci sequence of the first n numbers.  The fibonacci (f) of f(0) is 0 and of f(1) is 1.  The fibonacci of any other number is f(n-1) + f(n-2).  It has one extra block that is not needed in a correct solution.
   -----
   public int fibonacci(int n)
   {
   =====
       if(n == 0)
   =====
           return 0;
   =====
       else if(n == 1)
   =====
           return 1;
   =====
       else
   =====
           return fibonacci(n - 1) + fibonacci(n - 2);
   =====
   }
   =====
        return fibonacci(n - 1); #distractor