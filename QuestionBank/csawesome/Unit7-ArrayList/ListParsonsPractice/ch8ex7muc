.. parsonsprob:: ch8ex7muc
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
   :pct_on_first: 0.1300492611
   :total_students_attempting: 1015
   :num_students_correct: 826.0
   :mean_clicks_to_correct: 8.7590799031

   The following program segment is a method that should find the largest value given an ArrayList of Integers (the parameter) and move it to the back of the list.  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static void moveLargest(ArrayList<Integer> nums) {
   =====
       int largest = 0;
   =====
       for (int i = 0; i < nums.size(); i++) {
   =====
           if (nums.get(i) > nums.get(largest)) {
   =====
           if (nums[i] > nums[largest]) { #distractor
   =====
               largest = i;
   =====
           }
   =====
       } //end for loop
   =====
       Integer largestVal = nums.remove(largest);
       nums.add(largestVal);
   =====
       nums.add(largest); #distractor
   =====
   } //end moveLargest method