.. parsonsprob:: ch8ex8muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ListParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   The following method should remove all the Strings that have length 3 or shorter from an ArrayList of Strings (the parameter) -- so {"catch", "dog", "tree", "me"} should return {"catch", "tree"}.  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static void removeShort(ArrayList<String> words) {
   =====
       int i = 0;
   =====
       while (i < words.size()) {
   =====
           if (words.get(i).length() <= 3) {
   =====
           if (words.get(i).length <= 3) { #distractor
   =====
               words.remove(i);
   =====
           } else {
               i++;
           }
   =====
       } //end while loop
   =====
   } //end removeShort method