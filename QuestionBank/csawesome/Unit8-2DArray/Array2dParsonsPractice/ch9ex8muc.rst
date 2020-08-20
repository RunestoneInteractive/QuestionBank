.. parsonsprob:: ch9ex8muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dParsonsPractice
   :topics: Unit8-2DArray/Array2dParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.0580708661
   :total_students_attempting: 1016
   :num_students_correct: 852.0
   :mean_clicks_to_correct: 7.0164319249

   The following program segment is a method that should accept a two-dimensional int array and return a new two-dimensional int array containing only the odd index rows.  But, the blocks have been mixed up and include <b>three extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int[][] oddRows(int[][] nums) {
   =====
   public static int[] oddRows(int[][] nums) { #distractor
   =====
       int[][] odds = new int[nums.length / 2][nums[0].length];
   =====
       int[][] odds = new int[nums.length][nums[0].length]; #distractor
   =====
       int index = 0;
       for (int i = 0; i < nums.length; i++) {
   =====
           if (i % 2 == 1) {
   =====
               for (int j = 0; j < nums[i].length; j++) {
                   odds[index][j] = nums[i][j];
               }
   =====
               for (int j = 0; j < nums[i].length; j++) { #distractor
                   odds[index][j] = nums[j][i];
               }
   =====
               index++;
   =====
           } //end if
   =====
       } //end outer for loop
       return odds;
   } //end method