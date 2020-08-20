.. parsonsprob:: ch9ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: Array2dParsonsPractice
   :topics: Array2dBasics/Array2dParsonsPractice
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following program segment is a method that should accept a two-dimensional array of ints and edit it such that all even numbers are replaced by zero.  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static void makeEvenNumsZero(int[][] nums) {
   =====
       for (int row = 0; row < nums.length; row++) {
   =====
           for (int col = 0; col < nums[row].length; col++) {
   =====
           for (int col = 0; col < nums[row].length(); col++) { #distractor
   =====
               if (nums[row][col] % 2 == 0) {
                   nums[row][col] = 0;
               } //end if
   =====
               if (nums[row][col] % 2 == 1) { #distractor
                   nums[row][col] = 0;
               } //end if
   =====
           } //end inner for loop
   =====
       } //end outer for loop
   } //end method