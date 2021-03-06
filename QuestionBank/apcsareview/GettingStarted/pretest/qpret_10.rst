.. mchoice:: qpret_10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: The values don't matter this will always cause an infinite loop.
    :answer_b: Whenever a has values larger then temp.
    :answer_c: When all values in a are larger than temp.
    :answer_d: Whenever a includes a value that is less than or equal to zero.
    :answer_e: Whenever a includes a value equal to temp.
    :correct: d
    :feedback_a: An infinite loop will not always occur in this program segment. It occurs when at least one value in a is less than or equal to 0.
    :feedback_b: Values larger then temp will not cause an infinite loop.
    :feedback_c: Values larger then temp will not cause an infinite loop.
    :feedback_d: When a contains a value that is less than or equal to zero then multiplying that value by 2 will never make the result larger than the temp value (which was set to some value > 0), so an infinite loop will occur.
    :feedback_e: Values equal to temp will not cause the infinite loop.

    Which of the following will cause an infinite loop when ``temp`` is greater than zero and ``a`` is an array of integers.

    .. code-block:: java

        for (int k = 0; k < a.length; k++ )
        {
           while (a[k] < temp)
           {
              a[k] *= 2;
           }
        }