.. parsonsprob:: ch9ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit9-2DArray
   :subchapter: Array2dParsonsPractice
   :topics: Unit9-2DArray/Array2dParsonsPractice
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program segment is a method that should accept a two-dimensional int array and return the sum of all of its values.  But, the blocks have been mixed up and include <b>three extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int sumVals(int[][] nums) {
   =====
      int sum = 0;
   =====
      int sum; #distractor
   =====
      for (int row = 0; row < nums.length; row++) {
   =====
      for (int row = 0; row < nums.length(); row++) { #paired
   =====
            for (int col = 0; col < nums[row].length; col++) {
   =====
                sum += nums[row][col];
   =====
                sum = nums[row][col]; #paired
   =====
            } //end inner for loop
   =====
      } //end outer for loop
      return sum;
   =====
   } //end method