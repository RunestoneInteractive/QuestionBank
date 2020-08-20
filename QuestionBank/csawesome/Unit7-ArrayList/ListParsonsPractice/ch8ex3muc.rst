.. parsonsprob:: ch8ex3muc
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
   :pct_on_first: 0.1460032626
   :total_students_attempting: 1226
   :num_students_correct: 1089.0
   :mean_clicks_to_correct: 4.476584022

   The following program segment should remove all the zeros from an ArrayList of Integers.  Assume the ArrayList "listOfNums" has been instantiated and filled with Integers.  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   Integer zero = new Integer(0);
   int i = 0;
   =====
   while (i < listOfNums.size()) {
   =====
       if (listOfNums.get(i).equals(zero)) {
   =====
       if (listOfNums.get(i) == zero) { #distractor
   =====
           listOfNums.remove(i);
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