.. mchoice:: question8_5_1
   :author: bmiller
   :difficulty: 3.6621067031
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: CloningLists
   :topics: TransformingSequences/CloningLists
   :from_source: T
   :answer_a: [4,2,8,999,5,4,2,8,6,5]
   :answer_b: [4,2,8,999,5]
   :answer_c: [4,2,8,6,5]
   :correct: c
   :feedback_a: print alist not print blist
   :feedback_b: blist is changed, not alist.
   :feedback_c: Yes, alist was unchanged by the assignment statement. blist was a copy of the references in alist.
   :practice: T
   :pct_on_first: 0.3344733242
   :total_students_attempting: 1462
   :num_students_correct: 1450.0
   :mean_clicks_to_correct: 2.004137931

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4,2,8,6,5]
     blist = alist * 2
     blist[3] = 999
     print(alist)