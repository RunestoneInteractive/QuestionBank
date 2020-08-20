.. parsonsprob:: ch8ex3muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ListParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

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