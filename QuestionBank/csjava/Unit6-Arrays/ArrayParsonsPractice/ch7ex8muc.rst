.. parsonsprob:: ch7ex8muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/ArrayParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   The following program segment is a method that should return a new array of length 2 containing the middle two elements of a given array of integers of even length (the parameter) -- so {1,2,3,4} should return {2,3}.  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static int[] makeMiddle(int[] arr) {
   =====
       int[] result = new int[2];
   =====
       int middleIndex = (arr.length / 2) - 1;
   =====
       int middleIndex = (arr.length / 2); #distractor
   =====
       result[0] = arr[middleIndex];
       result[1] = arr[middleIndex + 1];
   =====
       return result;
   =====
   } //end makeMiddle method