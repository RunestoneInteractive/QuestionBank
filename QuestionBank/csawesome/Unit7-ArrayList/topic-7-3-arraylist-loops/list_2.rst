.. parsonsprob:: list_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0464344942
   :total_students_attempting: 3015
   :num_students_correct: 2585.0
   :mean_clicks_to_correct: 7.750483559

   The following has the correct code for a method called <code>insertInOrder</code> plus at least one extra unneeded code statement. This method should add the passed <code>name</code> in alphabetic order to a private list field called <code>nameList</code>.  Drag the needed blocks from the left into the correct order on the right. Check your solution by clicking on the <i>Check Me</i> button.  You will be told if any of the blocks are in the wrong order or if you need to remove one or more blocks.  There is one extra block that is not needed in a correct solution.
   -----
   public void insertInOrder(String name)
   {
   =====
     int index = 0;
   =====
     while (index < nameList.size() &&
            nameList.get(index).compareTo(name) < 0)
     {
   =====
       index++;
   =====
     } // end while
   =====
     nameList.add(index,name);
   =====
   } // end method
   =====
   nameList.add(name); #distractor