.. parsonsprob:: ch8ex4muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ListParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program segment is a method that should return the smallest int given an ArrayList of Integers (the parameter).  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static int findSmallest(ArrayList<Integer> nums) {
   =====
       int smallest = nums.get(0);
   =====
       int smallest = nums[0]; #distractor
   =====
       for (int i = 0; i < nums.size(); i++) {
   =====
           if (nums.get(i) < smallest) {
   =====
               smallest = nums.get(i);
   =====
           }
   =====
       } //end for loop
   =====
       return smallest;
   =====
   } //end findSmallest method