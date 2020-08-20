.. parsonsprob:: ch7ex4muc
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

   The following program segment is a method that should return the smallest integer given an array of integers (the parameter).  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static int findSmallest(int[] arr) {
   =====
       int smallest = arr[0];
   =====
       for (int i = 0 ; i < arr.length; i++) {
   =====
           if (arr[i] < smallest) {
   =====
           if (arr[i] > smallest) { #distractor
   =====
               smallest = arr[i];
   =====
           }
   =====
       } //end for loop
   =====
       return smallest;
   =====
   } //end findSmallest method