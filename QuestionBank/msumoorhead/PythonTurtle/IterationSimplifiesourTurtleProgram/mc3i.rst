.. mchoice:: mc3i
      :author: jenkins
      :difficulty: 3.0
      :basecourse: msumoorhead
      :chapter: PythonTurtle
      :subchapter: IterationSimplifiesourTurtleProgram
      :topics: PythonTurtle/IterationSimplifiesourTurtleProgram
      :from_source: None
      :answer_a: 2
      :answer_b: 4
      :answer_c: 5
      :answer_d: 1
      :correct: b
      :feedback_a: Python gives number the value of items in the list, one at a time, in order (from left to right).  number gets a new value each time the loop repeats.
      :feedback_b: Yes, Python will process the items from left to right so the first time the value of number is 5 and the second time it is 4.
      :feedback_c: Python gives number the value of items in the list, one at a time, in order.  number gets a new value each time the loop repeats.
      :feedback_d: Python gives number the value of items in the list, one at a time, in order (from left to right).  number gets a new value each time the loop repeats.

      In the following code, what is the value of number the second time Python executes the loop?

      .. code-block:: python

         for number in [5, 4, 3, 2, 1, 0]:
             print("I have", number, "cookies.  I'm going to eat one.")