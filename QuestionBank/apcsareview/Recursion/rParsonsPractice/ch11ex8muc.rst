.. parsonsprob:: ch11ex8muc
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rParsonsPractice
   :topics: Recursion/rParsonsPractice
   :from_source: F
   :noindent:
   :adaptive:

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