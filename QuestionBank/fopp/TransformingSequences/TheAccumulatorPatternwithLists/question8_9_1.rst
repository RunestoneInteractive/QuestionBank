.. mchoice:: question8_9_1
   :author: bmiller
   :difficulty: 1.9881656805
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: TheAccumulatorPatternwithLists
   :topics: TransformingSequences/TheAccumulatorPatternwithLists
   :from_source: T
   :answer_a: [4,2,8,6,5]
   :answer_b: [4,2,8,6,5,5]
   :answer_c: [9,7,13,11,10]
   :answer_d: Error, you cannot concatenate inside an append.
   :correct: c
   :feedback_a: 5 is added to each item before the append is performed.
   :feedback_b: There are too many items in this list. Only 5 append operations are performed.
   :feedback_c: Yes, the for loop processes each item of the list. 5 is added before it is appended to blist.
   :feedback_d: 5 is added to each item before the append operation is performed.
   :practice: T
   :pct_on_first: 0.7529585799
   :total_students_attempting: 1352
   :num_students_correct: 1344.0
   :mean_clicks_to_correct: 1.4047619048

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     blist = [ ]
     for item in alist:
        blist.append(item+5)
     print(blist)