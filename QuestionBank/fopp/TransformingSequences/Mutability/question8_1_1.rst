.. mchoice:: question8_1_1
   :author: bmiller
   :difficulty: 2.4194407457
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Mutability
   :topics: TransformingSequences/Mutability
   :from_source: T
   :answer_a: [4,2,True,8,6,5]
   :answer_b: [4,2,True,6,5]
   :answer_c: Error, it is illegal to assign
   :correct: b
   :feedback_a: Item assignment does not insert the new item into the list.
   :feedback_b: Yes, the value True is placed in the list at index 2. It replaces 8.
   :feedback_c: Item assignment is allowed with lists. Lists are mutable.
   :practice: T
   :pct_on_first: 0.6451398136
   :total_students_attempting: 1502
   :num_students_correct: 1497.0
   :mean_clicks_to_correct: 1.4595858383

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     alist[2] = True
     print(alist)