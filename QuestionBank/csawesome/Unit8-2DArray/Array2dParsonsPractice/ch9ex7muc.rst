.. parsonsprob:: ch9ex7muc
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
   :pct_on_first: 0.0243462579
   :total_students_attempting: 1109
   :num_students_correct: 936.0
   :mean_clicks_to_correct: 9.8717948718

   The following program segment is a method that should accept a two-dimensional int array and return a single dimensional (normal) int array containing the average of each of the columns.  But, the blocks have been mixed up and include <b>three extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int[] averageCols(int[][] nums) {
   =====
       int[] averages = new int[nums.length]; #distractor
   =====
       int[] averages = new int[nums[0].length];
   =====
       for (int col = 0; col < nums[0].length; col++) {
   =====
           int colSum = 0;
   =====
           for (int row = 0; row < nums.length; row++) {
               colSum += nums[row][col];
           } //end inner for loop
   =====
           for (int row = 0; row < nums.length; row++) { #distractor
               colSum += nums[col][row];
           } //end inner for loop
   =====
           averages[col] = colSum / nums.length;
   =====
           averages[col] = colSum / nums.length(); #distractor
   =====
       } //end outer for loop
       return averages;
   } //end method