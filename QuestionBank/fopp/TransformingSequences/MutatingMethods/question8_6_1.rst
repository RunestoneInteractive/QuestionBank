.. mchoice:: question8_6_1
   :author: bmiller
   :difficulty: 1.5269796776
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: MutatingMethods
   :topics: TransformingSequences/MutatingMethods
   :from_source: T
   :answer_a: [4,2,8,6,5,False,True]
   :answer_b: [4,2,8,6,5,True,False]
   :answer_c: [True,False,4,2,8,6,5]
   :correct: b
   :feedback_a: True was added first, then False was added last.
   :feedback_b: Yes, each item is added to the end of the list.
   :feedback_c: append adds at the end, not the beginning.
   :practice: T
   :pct_on_first: 0.8682550806
   :total_students_attempting: 1427
   :num_students_correct: 1421.0
   :mean_clicks_to_correct: 1.1604503871

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     alist.append(True)
     alist.append(False)
     print(alist)