.. parsonsprob:: pab_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.3237474059
   :total_students_attempting: 3373
   :num_students_correct: 3180.0
   :mean_clicks_to_correct: 3.1283018868

   The following program has the correct code to return the average of the first 3 items in the array a, but the code is mixed up.  Drag the blocks from the left into the correct order on the right. You will be told if any of the blocks are in the wrong order or are indented incorrectly.</p>
   -----
   public static double avg3(int[] a)
   {
   =====
     double total = 0;
   =====
     for (int i = 0; i < a.length && i < 3; i++)
     {
   =====
       total = total + a[i];
   =====
     } // end for
     return total / 3;
   =====
   } // end method