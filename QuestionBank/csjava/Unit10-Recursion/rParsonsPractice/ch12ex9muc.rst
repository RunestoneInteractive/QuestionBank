.. parsonsprob:: ch12ex9muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   The following method should return a string counting from 1 to the specified number -- so countTo(4) should return "1...2...3...4...".  But the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String countTo(int x)
   {
   =====
       if (x == 0)
       {
   =====
       if (x == 1) #distractor
       {
   =====
           return "";
   =====
       } //end if
       else
       {
   =====
           return countTo(x - 1) + x + "...";
   =====
           return countTo(x - 1) + (x - 1) + "..."; #distractor
   =====
       } //end else
   } //end method