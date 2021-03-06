.. mchoice:: qab_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :practice: T
   :answer_a: The values don't matter this will always cause an infinite loop.
   :answer_b: Whenever <i>a</i> includes a value that is less than or equal to zero.
   :answer_c: Whenever <i>a</i> has values larger then <i>temp</i>.
   :answer_d: When all values in <i>a</i> are larger than <i>temp</i>.
   :answer_e: Whenever <i>a</i> includes a value equal to <i>temp</i>.
   :correct: b
   :feedback_a: An infinite loop will not always occur in this code segment.
   :feedback_b: When <i>a</i> contains a value that is less than or equal to zero then multiplying that value by 2 will never make the result larger than the <i>temp</i> value (which was set to some value > 0), so an infinite loop will occur.
   :feedback_c: Values larger then <i>temp</i> will not cause an infinite loop.
   :feedback_d: Values larger then <i>temp</i> will not cause an infinite loop.
   :feedback_e: Values equal to <i>temp</i> will not cause the infinite loop.
   :pct_on_first: 0.4450934579
   :total_students_attempting: 3424
   :num_students_correct: 3374.0
   :mean_clicks_to_correct: 2.3992294013

   Given the following code segment, which of the following will cause an infinite loop?  Assume that ``temp`` is an int variable initialized to be greater than zero and that ``a`` is an array of integers.
   
   .. code-block:: java
   
      for ( int k = 0; k < a.length; k++ )
      {
         while ( a[ k ] < temp )
         {
            a[ k ] *= 2;
         }
      }