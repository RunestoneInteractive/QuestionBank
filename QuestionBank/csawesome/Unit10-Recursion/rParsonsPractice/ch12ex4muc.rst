.. parsonsprob:: ch12ex4muc
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
   :pct_on_first: 0.0286975717
   :total_students_attempting: 453
   :num_students_correct: 419.0
   :mean_clicks_to_correct: 6.0787589499

   The following method should remove any occurrence of an asterisk "*" from a passed-in string -- so "ab*c**d" should become "abcd".  But the blocks have been mixed up.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String removeStar(String myText)
   {
   =====
       if (myText.length() == 0)
       {
          return "";
       } //end if
   =====
       else
       {
   =====
         if (myText.charAt(0) == '*')
         {
            return removeStar(myText.substring(1));
         } //end if
   =====
         return myText.charAt(0) + removeStar(myText.substring(1));
   =====
       } //end else
   } //end method