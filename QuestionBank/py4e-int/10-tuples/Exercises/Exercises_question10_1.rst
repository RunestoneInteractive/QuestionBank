.. mchoice:: Exercises_question10_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: Exercises
   :topics: 10-tuples/Exercises
   :from_source: T
   :practice: T
   :answer_a: aTuple[1:2][1]
   :answer_b: aTuple[2][1]
   :answer_c: aTuple[1:2](1)
   :answer_d: aTuple[1][1]
   :correct: d
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Try again!
   :feedback_d: Correct! This first goes to the second item in the tuple, then grabs the second item from the list, which is 20.

   Choose the correct way to access the value 20 from the following tuple.

   .. code-block:: python

      aTuple = ("Orange", [10, 20, 30], (5, 15, 25))