.. parsonsprob:: ch12ex8muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rParsonsPractice
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :noindent: 
   :adaptive: 
   :pct_on_first: 0.3438256659
   :total_students_attempting: 413
   :num_students_correct: 379.0
   :mean_clicks_to_correct: 2.7678100264

   The following method should return number of times the character " x " is in a String -- so findNumX("xHihxixx") should return 4.  But the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int findNumX(String s)
   {
   =====
       if (s.length() == 0)
       {
           return 0;
       } //end if
   =====
       else
       {
   =====
           if (s.charAt(0) == 'x')
           {
               return 1 + findNumX(s.substring(1));
           } //end if
   =====
           if (s.charAt(0) = 'x') #distractor
           {
               return 1 + findNumX(s.substring(0));
           } //end if
   =====
           return findNumX(s.substring(1));
   =====
       } //end else
   } //end method