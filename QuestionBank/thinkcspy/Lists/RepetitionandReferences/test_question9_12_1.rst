.. mchoice:: test_question9_12_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: RepetitionandReferences
   :topics: Lists/RepetitionandReferences
   :from_source: T
   :practice: T
   :answer_a: [4, 2, 8, 999, 5, 4, 2, 8, 6, 5]
   :answer_b: [4, 2, 8, 999, 5]
   :answer_c: [4, 2, 8, 6, 5]
   :correct: c
   :feedback_a: print(alist) not print(blist)
   :feedback_b: blist is changed, not alist.
   :feedback_c: Yes, alist was unchanged by the assignment statement. blist was a copy of the references in alist.
   :pct_on_first: 0.2832983088
   :total_students_attempting: 9993
   :num_students_correct: 9940.0
   :mean_clicks_to_correct: 2.0769617706

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4, 2, 8, 6, 5]
     blist = alist * 2
     blist[3] = 999
     print(alist)