.. mchoice:: mc8l
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: TheAccumulatorPatternwithStrings
   :topics: Strings/TheAccumulatorPatternwithStrings
   :from_source: None
   :answer_a: BALLBALLBALLBALL
   :answer_b: BALL
   :answer_c: LLAB
   :correct: c
   :feedback_a: item is a single character.
   :feedback_b: The order is wrong.
   :feedback_c: Yes, the order is reversed due to the order of the concatenation.

   What is printed by the following statements:

   .. code-block:: python

      s = "BALL"
      r = ""
      for item in s:
          r = item + r
      print(r)