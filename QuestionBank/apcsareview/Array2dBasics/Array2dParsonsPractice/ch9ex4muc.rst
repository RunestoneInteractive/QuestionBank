.. parsonsprob:: ch9ex4muc
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

   The following program segment is a method that should accept a two-dimensional String array "image" and flip the "image" 180 degrees vertically. For example:  </br>

   1 2 3 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 3 2 1 </br>
   1 2 3 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 3 2 1 </br>
   1 2 3 4&nbsp;&nbsp;->&nbsp;&nbsp;4 3 2 1 </br>
   1 2 3 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 3 2 1 </br>

   But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static void flipImage(String[][] image) {
   =====
       for (int row = 0; row < image.length; row++) {
   =====
           for (int col = 0; col < image[0].length / 2; col++) {
   =====
               String temp = image[row][col];
               image[row][col] = image[row][image.length - 1 - col];
               image[row][image.length - 1 - col] = temp;
   =====
               image[row][col] = image[row][image.length - 1 - col]; #paired
               image[row][image.length - 1 - col] = image[row][col];
   =====
           } //end inner for loop
       } //end outer for loop
   } //end method