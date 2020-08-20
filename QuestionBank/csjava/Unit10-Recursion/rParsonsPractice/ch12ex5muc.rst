.. parsonsprob:: ch12ex5muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :noindent:
   :adaptive:

   The following method should return the base multiplied power times. In otherwords, the base ^ power -- so exponent(2, 4) should return 16.  But the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int exponent(int base, int power)
   {
   =====
       if (power == 0)
       {
   =====
           return 1;
   =====
           return 0; #distractor
   =====
       } //end if
       else
       {
   =====
           return base * exponent(base, power - 1);
   =====
       } //end else
   } //end method