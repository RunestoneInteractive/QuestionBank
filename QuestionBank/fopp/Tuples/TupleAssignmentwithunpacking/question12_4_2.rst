.. mchoice:: question12_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Tuples
   :subchapter: TupleAssignmentwithunpacking
   :topics: Tuples/TupleAssignmentwithunpacking
   :from_source: T
   :practice: T
   :answer_a: You can't use different variable names on the left and right side of an assignment statement.
   :answer_b: At the end, x still has it's original value instead of y's original value.
   :answer_c: Actually, it works just fine!
   :feedback_a: Sure you can; you can use any variable on the right-hand side that already has a value.
   :feedback_b: Once you assign x's value to y, y's original value is gone.
   :feedback_c: Once you assign x's value to y, y's original value is gone.
   :correct: b
   :pct_on_first: 0.69476082
   :total_students_attempting: 439
   :num_students_correct: 432.0
   :mean_clicks_to_correct: 1.3564814815

   Consider the following alternative way to swap the values of variables x and y. What's wrong with it?
   
   .. code-block:: python
   
        # assume x and y already have values assigned to them
        y = x
        x = y