.. mchoice:: test_question9_12_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: RepetitionandReferences
   :topics: Lists/RepetitionandReferences
   :from_source: T
   :practice: T
   :answer_a: [4, 2, 8, 999, 5, 4, 2, 8, 999, 5]
   :answer_b: [[4, 2, 8, 999, 5], [4, 2, 8, 999, 5]]
   :answer_c: [4, 2, 8, 6, 5]
   :answer_d: [[4, 2, 8, 999, 5], [4, 2, 8, 6, 5]]
   :correct: b
   :feedback_a: [alist] * 2 creates a list containing alist repeated 2 times
   :feedback_b: Yes, blist contains two references, both to alist.
   :feedback_c: print(blist)
   :feedback_d: blist contains two references, both to alist so changes to alist appear both times.
   :pct_on_first: 0.6217871486
   :total_students_attempting: 9960
   :num_students_correct: 9908.0
   :mean_clicks_to_correct: 1.5567218409

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4, 2, 8, 6, 5]
     blist = [alist] * 2
     alist[3] = 999
     print(blist)