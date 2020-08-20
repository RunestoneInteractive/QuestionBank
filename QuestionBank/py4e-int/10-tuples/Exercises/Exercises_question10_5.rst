.. mchoice:: Exercises_question10_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: Exercises
   :topics: 10-tuples/Exercises
   :from_source: T
   :practice: T
   :answer_a: TypeError
   :answer_b: (100, 800, 200, 300, 400, 500)
   :answer_c: (800, 100, 200, 300, 400, 500)
   :answer_d: (100, 200, 800, 300, 400, 500)
   :correct: a
   :feedback_a: Correct! A tuple is immutable, therefore you cannot change its values.
   :feedback_b: Try again!
   :feedback_c: Try again!
   :feedback_d: Try again!

   What is printed when the following code is run?

   .. code-block:: python

      aTuple = (100, 200, 300, 400, 500)
      aTuple[1] = 800
      print(aTuple)