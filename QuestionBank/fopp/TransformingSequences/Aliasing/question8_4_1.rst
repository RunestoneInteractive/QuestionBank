.. mchoice:: question8_4_1
   :author: bmiller
   :difficulty: 1.8958475153
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Aliasing
   :topics: TransformingSequences/Aliasing
   :from_source: T
   :answer_a: [4,2,8,6,5]
   :answer_b: [4,2,8,999,5]
   :correct: b
   :feedback_a: blist is not a copy of alist, it is a reference to the list alist refers to.
   :feedback_b: Yes, since alist and blist both reference the same list, changes to one also change the other.
   :practice: T
   :pct_on_first: 0.7760381212
   :total_students_attempting: 1469
   :num_students_correct: 1459.0
   :mean_clicks_to_correct: 1.2302947224

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     blist = alist
     blist[3] = 999
     print(alist)