.. parsonsprob:: ch7ex9muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: ArrayParsonsPractice
   :topics: Unit7-Arrays/ArrayParsonsPractice
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:

   The following program segment is a method that should return string array that is in reverse order -- so {"b", "a", "z"} should return {"z", "a", "b"}.  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static String[] reverse(String[] arr) {
   =====
       String[] result = new String[arr.length];
   =====
       int i = arr.length - 1;
   =====
       int i = arr.length; #distractor
   =====
       for (String element: arr) {
   =====
       for (element: arr) { #distractor
   =====
         result[i] = element;
   =====
         i--;
   =====
       } //end for loop
   =====
       return result;
   =====
   } //end reverse method