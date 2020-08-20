.. parsonsprob:: ch12ex2muc
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
   :pct_on_first: 0.2345679012
   :total_students_attempting: 486
   :num_students_correct: 459.0
   :mean_clicks_to_correct: 3.9215686275

   The following method should multiply the two passed-in positive integers (using the fact that multiplcation is repeated addition) -- so multipy(3, 4) should become 12 (3+3+3+3).  But the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int multiply(int a, int b)
   {
   =====
       if (b == 0)
       {
   =====
         return 0;
   =====
         return 1; #distractor
   =====
       } //end if
   =====
       else
       {
   =====
         return multiply(a, b - 1) + a;
   =====
       } //end else
   } //end method