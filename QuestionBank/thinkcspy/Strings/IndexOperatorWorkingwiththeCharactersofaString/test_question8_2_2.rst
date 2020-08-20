.. mchoice:: test_question8_2_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: IndexOperatorWorkingwiththeCharactersofaString
   :topics: Strings/IndexOperatorWorkingwiththeCharactersofaString
   :from_source: T
   :practice: T
   :answer_a: tr
   :answer_b: ps
   :answer_c: nn
   :answer_d: Error, you cannot use the [ ] operator with the + operator.
   :correct: a
   :feedback_a: Yes, indexing operator has precedence over concatenation.
   :feedback_b: p is at location 0, not 2.
   :feedback_c: n is at location 5, not 2.
   :feedback_d: [ ] operator returns a string that can be concatenated with another string.
   :pct_on_first: 0.8787018256
   :total_students_attempting: 12325
   :num_students_correct: 12274.0
   :mean_clicks_to_correct: 1.2139481832

   
   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s[2] + s[-5])