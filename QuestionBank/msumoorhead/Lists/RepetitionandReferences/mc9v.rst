.. mchoice:: mc9v
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: RepetitionandReferences
   :topics: Lists/RepetitionandReferences
   :from_source: None
   :answer_a: [4, 2, 8, 999, 5, 4, 2, 8, 999, 5]
   :answer_b: [[4, 2, 8, 999, 5], [4, 2, 8, 999, 5]]
   :answer_c: [4, 2, 8, 6, 5]
   :answer_d: [[4, 2, 8, 999, 5], [4, 2, 8, 6, 5]]
   :correct: b
   :feedback_a: [alist] * 2 creates a list containing alist repeated 2 times
   :feedback_b: Yes, blist contains two references, both to alist.
   :feedback_c: print(blist)
   :feedback_d: blist contains two references, both to alist so changes to alist appear both times.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     blist = [alist] * 2
     alist[3] = 999
     print(blist)