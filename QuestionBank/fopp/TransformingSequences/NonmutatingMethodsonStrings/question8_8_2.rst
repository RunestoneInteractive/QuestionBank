.. mchoice:: question8_8_2
   :author: bmiller
   :difficulty: 3.0663780664
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: NonmutatingMethodsonStrings
   :topics: TransformingSequences/NonmutatingMethodsonStrings
   :from_source: T
   :answer_a: yyyyy
   :answer_b: 55555
   :answer_c: n
   :answer_d: Error, you cannot combine all those things together.
   :correct: a
   :feedback_a: Yes, s[1] is y and the index of n is 5, so 5 y characters.  It is important to realize that the index method has precedence over the repetition operator.  Repetition is done last.
   :feedback_b: Close.  5 is not repeated, it is the number of times to repeat.
   :feedback_c: This expression uses the index of n
   :feedback_d: This is fine, the repetition operator used the result of indexing and the index method.
   :practice: T
   :pct_on_first: 0.4834054834
   :total_students_attempting: 1386
   :num_students_correct: 1377.0
   :mean_clicks_to_correct: 1.966594045

   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s[1]*s.index("n"))