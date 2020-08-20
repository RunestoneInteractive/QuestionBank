.. mchoice:: question6_5_3
      :author: bmiller
      :difficulty: 4.011011011
      :basecourse: fopp
      :chapter: Iteration
      :subchapter: Listsandforloops
      :topics: Iteration/Listsandforloops
      :from_source: T
      :answer_a: Draw a square using the same color for each side.
      :answer_b: Draw a square using a different color for each side.
      :answer_c: Draw one side of a square.
      :correct: c
      :feedback_a: The question is not asking you to describe the outcome of the entire loop, the question is asking you about the outcome of a **single iteration** of the loop.
      :feedback_b: Notice that aColor is never actually used inside the loop.
      :feedback_c: The body of the loop only draws one side of the square.  It will be repeated once for each item in the list.  However, the color of the turtle never changes.
      :pct_on_first: 0.2472472472
      :total_students_attempting: 1998
      :num_students_correct: 1972.0
      :mean_clicks_to_correct: 2.0770791075

      Consider the following code:
      
      .. code-block:: python
      
        for aColor in ["yellow", "red", "green", "blue"]:
           alex.forward(50)
           alex.left(90)
      
      What does each iteration through the loop do?