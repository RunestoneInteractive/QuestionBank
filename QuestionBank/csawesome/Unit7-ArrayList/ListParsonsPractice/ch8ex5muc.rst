.. parsonsprob:: ch8ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ListParsonsPractice
   :topics: Unit7-ArrayList/ListParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.5194444444
   :total_students_attempting: 1080
   :num_students_correct: 944.0
   :mean_clicks_to_correct: 2.094279661

   The following program segment is a method that should remove all the positive and negative odd values in an ArrayList of Integers (the parameter).  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static void removeOdd(ArrayList<Integer> nums) {
   =====
       int i = 0;
   =====
       while (i < nums.size()) {
   =====
           if (Math.abs(nums.get(i)) % 2 == 1) {
   =====
           if (nums.get(i) % 2 == 1) { #distractor
   =====
               nums.remove(i);
   =====
           } else {
               i++;
           }
   =====
       } //end while loop
   =====
   } //end removeOdd method