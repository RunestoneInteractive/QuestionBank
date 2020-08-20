.. mchoice:: question8_1_3
   :author: bmiller
   :difficulty: 2.1186903138
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Aliasing
   :topics: TransformingSequences/Aliasing
   :from_source: T
   :answer_a: ['Jamboree', 'get-together', 'party']
   :answer_b: ['celebration']
   :answer_c: ['celebration', 'Jamboree', 'get-together', 'party']
   :answer_d: ['Jamboree', 'get-together', 'party', 'celebration']
   :correct: a
   :feedback_a: Yes, the value of y has been reassigned to the value of w.
   :feedback_b: No, that was the inital value of y, but y has changed.
   :feedback_c: No, when we assign a list to another list it does not concatenate the lists together.
   :feedback_d: No, when we assign a list to another list it does not concatenate the lists together.
   :practice: T
   :pct_on_first: 0.7203274216
   :total_students_attempting: 1466
   :num_students_correct: 1458.0
   :mean_clicks_to_correct: 1.5576131687

   What is the value of y after the following code has been evaluated:
   
   .. code-block:: python
   
      w = ['Jamboree', 'get-together', 'party']
      y = ['celebration']
      y = w