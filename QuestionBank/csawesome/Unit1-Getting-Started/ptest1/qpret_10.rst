.. mchoice:: qpret_10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit1-Getting-Started
    :subchapter: ptest1
    :topics: Unit1-Getting-Started/ptest1
    :from_source: T
    :answer_a: The values don't matter this will always cause an infinite loop.
    :answer_b: Whenever a has values larger than temp.
    :answer_c: When all values in a are larger than temp.
    :answer_d: Whenever a includes a value that is equal to zero.
    :answer_e: Whenever a includes a value equal to temp.
    :correct: d
    :feedback_a: An infinite loop will not always occur in this program segment. It occurs when at least one value in a is less than or equal to 0.
    :feedback_b: Values larger then temp will not cause an infinite loop.
    :feedback_c: Values larger then temp will not cause an infinite loop.
    :feedback_d: When a contains a value that is equal to zero then multiplying that value by 2 will always be 0 and will never make the result larger than the temp value (which was set to some value > 0), so an infinite loop will occur.
    :feedback_e: Values equal to temp will not cause the infinite loop.
    :pct_on_first: 0.341633823
    :total_students_attempting: 5582
    :num_students_correct: 2267.0
    :mean_clicks_to_correct: 1.3511248346

    Which of the following will cause an infinite loop when ``temp`` is greater than zero and ``a`` is an array of integers.
    
    .. code-block:: java
    
        for (int k = 0; k < a.length; k++ )
        {
           while (a[k] < temp)
           {
              a[k] *= 2;
           }
        }