.. parsonsprob:: ch9ex2muc
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

   The following program segment should create a 8 by 8 two-dimensional int array. It should fill this array with a checkered pattern of 0s and 1s -- starting with a 1 in the top left corner and print the output (in row-column order).  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   int[][] checkerboard = new int[8][8];
   =====
   for (int row = 0; row < checkerboard.length; row++) {
       for (int col = 0; col < checkerboard[row].length; col++) {
   =====
           if ( (row + col) % 2 == 0) {
   =====
           if ( (row + col) % 2 == 1) { #paired
   =====
               checkerboard[row][col] = 1;
   =====
           } //end if
   =====
           System.out.print(checkerboard[row][col] + " ");
   =====
       } //end inner for loop
   } //end outer for loop