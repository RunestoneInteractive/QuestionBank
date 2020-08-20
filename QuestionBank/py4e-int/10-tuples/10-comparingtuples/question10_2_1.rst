.. mchoice:: question10_2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-comparingtuples
   :topics: 10-tuples/10-comparingtuples
   :from_source: T
   :practice: T
   :answer_a: True
   :answer_b: False
   :answer_c: An error message will occur
   :correct: a
   :feedback_a: Correct! The comparison operator will look up to the first pair of elements that differ from each other. In this case it is the first element, so all preceding elements are ignored.
   :feedback_b: Try again!
   :feedback_c: Try again!

   What is returned when the following code is run?

   .. code-block:: python

      (5, 7, 3) < (7, 4, 2)