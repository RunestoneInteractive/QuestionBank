.. parsonsprob:: pab_1r
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following method has the correct code to subtract amt from all the values in the array <b>values</b>, but the code is mixed up.  Drag the blocks from the left into the correct order on the right. You will be told if any of the blocks are in the wrong order.
   -----
   public static void subAll(int[] values, int amt)
   {
   =====
        for (int i = 0;
   =====
           i < values.length;
   =====
           i++)
   =====
      {
   =====
         values[i] = values[i] - amt;
   =====
      } // end for loop
   =====
   } // end method