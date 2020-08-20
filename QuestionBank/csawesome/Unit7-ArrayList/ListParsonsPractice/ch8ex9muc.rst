.. parsonsprob:: ch8ex9muc
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
   :pct_on_first: 0.2354740061
   :total_students_attempting: 981
   :num_students_correct: 824.0
   :mean_clicks_to_correct: 3.6516990291

   The following program segment is a method that should take each String from an ArrayList of Strings (the parameter) and add it again to the list -- so {"cat", "ribbon", "house"} should become {"cat", "cat", "ribbon", "ribbon", "house", "house"}.  But, the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static void doubleList(ArrayList<String> words) {
   =====
       int count = 0;
   =====
       while (count < words.size()) {
   =====
       while (count <= words.size()) { #distractor
   =====
           String toAdd = words.get(count);
           words.add(count, toAdd);
   =====
           count += 2;
   =====
           count++; #distractor
   =====
       } //end while loop
   =====
   } //end doubleList method