.. parsonsprob:: ch9ex1muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit8-2DArray/Array2dParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program segment should create a 10 by 10 two-dimensional int array. It should fill this array with numbers 0 to 99 from left to right, top row to bottom row and print the output (in row-column order).  But, the blocks have been mixed up and contain an extra block that is not needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   int[][] table = new int[10][10];
   =====
   for (int row = 0; row < table.length; row++) {
       for (int col = 0; col < table[row].length; col++) {
   =====
           table[row][col] = col + 10 * row;
   =====
           table[row][col] = row + 10 * col; #paired
   =====
           System.out.print(table[row][col] + "\t");
   =====
       } //end inner for loop
   } //end outer for loop