.. parsonsprob:: ch9ex10muc
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
   :pct_on_first: 0.1971971972
   :total_students_attempting: 999
   :num_students_correct: 857.0
   :mean_clicks_to_correct: 4.016336056

   The following program segment is a method that should accept a two-dimensional int array, and return a single-dimensional (normal) int array containing the max of each row.  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int[] maxEachRow(int[][] nums) {
   =====
      int[] max = new int[nums.length];
   =====
      for (int i = 0; i < nums.length; i++) {
   =====
          int maxVal = nums[i][0];
          for (int j = 1; j < nums[i].length; j++) {
   =====
              if (maxVal < nums[i][j]) {
                  maxVal = nums[i][j];
              }
   =====
              if (maxVal > nums[i][j]) { #distractor
                  maxVal = nums[i][j];
              }
   =====
          } //end inner for loop
          max[i] = maxVal;
   =====
      } //end outer for loop
      return max;
   } //end method