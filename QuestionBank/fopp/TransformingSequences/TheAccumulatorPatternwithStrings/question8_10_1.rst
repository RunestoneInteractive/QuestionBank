.. mchoice:: question8_10_1
   :author: bmiller
   :difficulty: 4.0736522399
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: TheAccumulatorPatternwithStrings
   :topics: TransformingSequences/TheAccumulatorPatternwithStrings
   :from_source: T
   :answer_a: Ball
   :answer_b: BALL
   :answer_c: LLAB
   :correct: c
   :feedback_a: Each item is converted to upper case before concatenation.
   :feedback_b: Each character is converted to upper case but the order is wrong.
   :feedback_c: Yes, the order is reversed due to the order of the concatenation.
   :practice: T
   :pct_on_first: 0.23158694
   :total_students_attempting: 1317
   :num_students_correct: 1306.0
   :mean_clicks_to_correct: 1.9517611026

   What is printed by the following statements:
   
   .. code-block:: python
   
      s = "ball"
      r = ""
      for item in s:
         r = item.upper() + r
      print(r)