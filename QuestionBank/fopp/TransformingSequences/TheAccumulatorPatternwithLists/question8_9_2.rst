.. mchoice:: question8_9_2
   :author: bmiller
   :difficulty: 2.3054518297
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: TheAccumulatorPatternwithLists
   :topics: TransformingSequences/TheAccumulatorPatternwithLists
   :from_source: T
   :answer_a: [8,5,14,9,6]
   :answer_b: [8,5,14,9,6,12]
   :answer_c: [3,0,9,4,1,7,5]
   :answer_d: Error, you cannot concatenate inside an append.
   :correct: b
   :feedback_a: Don't forget the last item!
   :feedback_b: Yes, the for loop processes each item in lst. 5 is added before lst[i] is appended to new_list.
   :feedback_c: 5 is added to each item before the append operation is performed.
   :feedback_d: It is OK to have a complex expression inside the call to the append method. The expression `lst[i]+5` is fully evaluated before the append operation is performed.
   :practice: T
   :pct_on_first: 0.6736370426
   :total_students_attempting: 1339
   :num_students_correct: 1332.0
   :mean_clicks_to_correct: 1.4444444444

   What is printed by the following statements?
   
   .. code-block:: python
   
     lst= [3,0,9,4,1,7]
     new_list=[]
     for i in range(len(lst)):
        new_list.append(lst[i]+5)
     print(new_list)