.. parsonsprob:: ch11ex10muc
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rParsonsPractice
   :topics: Recursion/rParsonsPractice
   :from_source: F
   :noindent:
   :adaptive:

   The following method should take an passed-in number and return a string such that only the even numbers are still present. All of the odd digits should be replaced with a "_" -- so 4321 should become "4_2_".  But the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String displayEvenDigits(int num)
   {
   =====
       if (num == 0)
       {
           return "";
       } //end if
   =====
       else
       {
   =====
           if ((num % 10) % 2 == 0)
           {
   =====
           if ((num % 10) % 2 == 1) #distractor
           {
   =====
               return "" + displayEvenDigits(num / 10) + (num % 10);
           } //end if
   =====
           return displayEvenDigits(num / 10) + "_";
   =====
           return "_" + displayEvenDigits(num / 10); #distractor
   =====
       } //end else
   } //end method