.. parsonsprob:: pab_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aForEach
   :topics: ArrayBasics/aForEach
   :from_source: T
   :numbered: left
   :adaptive:

   The following method has the correct code to return the largest value in an integer array called <i>vals</i> (a field of the current object), but the code is mixed up.  Drag the blocks from the left into the correct order on the right and indent them correctly as well. You will be told if any of the blocks are in the wrong order or not indented correctly.</p>
   -----
   public int getLargest()
   {
   =====
     int largest = vals[0];
   =====
     for (int item : vals)
     {
   =====
       if (item > largest)
       {
   =====
         largest = item;
   =====
       }  // end if
   =====
     } // end for
     return largest;
   =====
   } // end method