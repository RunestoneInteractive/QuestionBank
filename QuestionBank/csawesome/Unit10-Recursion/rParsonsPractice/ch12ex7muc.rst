.. parsonsprob:: ch12ex7muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rParsonsPractice
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.3627684964
   :total_students_attempting: 419
   :num_students_correct: 387.0
   :mean_clicks_to_correct: 2.9121447028

   The following method should repeat the passed-in string a set number of times -- so repeatThis("hi", 3) should return "hihihi".  But the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String repeatThis(String s, int i)
   {
   =====
       if (i == 0)
       {
   =====
       if (i >= 0) #distractor
       {
   =====
          return "";
   =====
       } //end if
       else
       {
   =====
          return s + repeatThis(s, i-1);
   =====
          return repeatThis(s, i-1); #distractor
   =====
       } //end else
   } //end method