.. parsonsprob:: ch7ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: ArrayParsonsPractice
   :topics: ArrayBasics/ArrayParsonsPractice
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following program segment should print each element in the array that is even.  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   int[] arr = {14, -5, 2, 17, 29, -8, 36};
   =====
   for (int i = 0; i < arr.length; i++) {
   =====
       if (arr[i] % 2 == 0) {
   =====
           System.out.println(arr[i]);
   =====
       } //end conditional
   =====
   } //end for loop