.. parsonsprob:: pab_1r
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aLoopFrontToBack
   :topics: ArrayBasics/aLoopFrontToBack
   :from_source: T
   :numbered: left
   :adaptive:

   The following method has the correct code to subtract amt from all the values in the array <b>values</b> (a field of the current object), but the code is mixed up.  Drag the blocks from the left into the correct order on the right and indent them correctly. You will be told if any of the blocks are in the wrong order or not indented correctly.
   -----
   public void subAll(int amt)
   {
   =====
      for (int i = 0;
           i < values.length;
           i++)
      {
   =====
         values[i] = values[i] - amt;
   =====
      } // end for loop
   =====
   } // end method