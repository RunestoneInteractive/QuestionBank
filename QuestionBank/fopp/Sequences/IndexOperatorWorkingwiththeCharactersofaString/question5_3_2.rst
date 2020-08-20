.. mchoice:: question5_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: IndexOperatorWorkingwiththeCharactersofaString
   :topics: Sequences/IndexOperatorWorkingwiththeCharactersofaString
   :from_source: T
   :answer_a: tr
   :answer_b: to
   :answer_c: ps
   :answer_d: nn
   :answer_e: Error, you cannot use the [ ] operator with the + operator.
   :correct: b
   :feedback_a: Almost, t is at postion 2, counting left to right starting from 0; but r is at -5, counting right to left starting from -1.
   :feedback_b: For -4 you count from right to left, starting with -1.
   :feedback_c: p is at location 0, not 2.
   :feedback_d: n is at location 5, not 2.
   :feedback_e: [ ] operator returns a string that can be concatenated with another string.
   :practice: T
   :pct_on_first: 0.7205882353
   :total_students_attempting: 2312
   :num_students_correct: 2300.0
   :mean_clicks_to_correct: 1.4504347826

   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s[2] + s[-4])