.. parsonsprob:: list_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listLoop
   :topics: ListBasics/listLoop
   :from_source: T
   :numbered: left
   :adaptive:

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