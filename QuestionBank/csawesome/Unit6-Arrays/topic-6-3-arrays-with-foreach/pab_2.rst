.. parsonsprob:: pab_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit6-Arrays/topic-6-3-arrays-with-foreach
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.2574886536
   :total_students_attempting: 3305
   :num_students_correct: 3035.0
   :mean_clicks_to_correct: 4.8184514003

   The following method has the correct code to return the largest value in an integer array called <i>vals</i> (an instance variable of the current object), but the code is mixed up.  Drag the blocks from the left into the correct order on the right and indent them correctly as well. You will be told if any of the blocks are in the wrong order or not indented correctly.</p>
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