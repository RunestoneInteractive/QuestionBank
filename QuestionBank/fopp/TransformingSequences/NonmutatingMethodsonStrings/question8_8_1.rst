.. mchoice:: question8_8_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: NonmutatingMethodsonStrings
   :topics: TransformingSequences/NonmutatingMethodsonStrings
   :from_source: T
   :answer_a: 0
   :answer_b: 2
   :answer_c: 3
   :correct: c
   :feedback_a: There are definitely o and p characters.
   :feedback_b: There are 2 o characters but what about p?
   :feedback_c: Yes, add the number of o characters and the number of p characters.
   :practice: T
   :pct_on_first: 0.8067528736
   :total_students_attempting: 1392
   :num_students_correct: 1385.0
   :mean_clicks_to_correct: 1.2519855596

   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s.count("o") + s.count("p"))