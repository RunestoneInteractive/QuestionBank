.. parsonsprob:: ch7ex6muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/ArrayParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   The following program segment is a method that should return the largest integer given an array of integers (the parameter).  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static int findLargest(int[] arr) {
   =====
      int largest = arr[0];
   =====
      int largest = arr.get(0); #distractor
   =====
      for (int i = 0; i < arr.length; i++) {
   =====
          if (largest < arr[i]) {
   =====
          if (largest > arr[i]) { #distractor
   =====
              largest = arr[i];
   =====
          } //end conditional
   =====
      } //end for loop
   =====
      return largest;
   =====
   } //end findLargest method