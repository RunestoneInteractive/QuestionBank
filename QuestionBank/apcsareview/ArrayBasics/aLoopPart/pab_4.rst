.. parsonsprob:: pab_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aLoopPart
   :topics: ArrayBasics/aLoopPart
   :from_source: T
   :numbered: left
   :adaptive:

   The following program has the correct code to return the average of the first 3 items in the array a, but the code is mixed up.  Drag the blocks from the left into the correct order on the right. You will be told if any of the blocks are in the wrong order or are indented incorrectly.</p>
   -----
   public double avg3()
   {
   =====
     double total = 0;
     for (int i = 0;
          i < a.length && i < 3;
          i++)
     {
   =====
       total = total + a[i];
   =====
     } // end for
     return total / 3;
   =====
   } // end method