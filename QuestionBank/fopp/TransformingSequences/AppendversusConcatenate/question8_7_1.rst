.. mchoice:: question8_7_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: AppendversusConcatenate
   :topics: TransformingSequences/AppendversusConcatenate
   :from_source: T
   :answer_a: [4,2,8,6,5,999]
   :answer_b: Error, you cannot concatenate a list with an integer.
   :correct: b
   :feedback_a: You cannot concatenate a list with an integer.
   :feedback_b: Yes, in order to perform concatenation you would need to write alist+[999].  You must have two lists.
   :practice: T
   :pct_on_first: 0.473796034
   :total_students_attempting: 1412
   :num_students_correct: 1391.0
   :mean_clicks_to_correct: 1.5406182602

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     alist = alist + 999
     print(alist)