.. parsonsprob:: ch12ex1muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit11-Recursion
   :subchapter: rParsonsPractice
   :topics: Unit11-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :noindent:
   :adaptive:

   The following method should reverse the order of the characters in the given string -- so "abcd" should become "dcba".  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String reverse(String myText)
   {
       if (myText.length() == 0)
       {
   =====
           return "";
   =====
       } //end if
   =====
       else
       {
   =====
           return reverse(myText.substring(1)) + myText.charAt(0);
   =====
       } //end else
   } //end method