.. parsonsprob:: ch8ex10muc
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
   :pct_on_first: 0.2097297297
   :total_students_attempting: 925
   :num_students_correct: 763.0
   :mean_clicks_to_correct: 3.9436435125

   The following method should remove a specific Integer (specified in parameter) whenever it occurs in a given ArrayList of Integers (the parameter).  But, the blocks have been mixed up and include <b>three extra blocks</b> that are not needed in a correct solution.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static void removeElement(ArrayList<Integer> nums,
                                    int toRemove) {
   =====
      int i = 0;
   =====
      while (i < nums.size()) {
   =====
      while (i < nums.length) { #distractor
   =====
          if (nums.get(i) == toRemove) {
   =====
          if (nums.get(i) == nums(toRemove)) { #distractor
   =====
           nums.remove(i);
   =====
          } //end if
   =====
          else {
              i++;
          }
   =====
          i++; #distractor
   =====
      } //end while loop
   } //end average method