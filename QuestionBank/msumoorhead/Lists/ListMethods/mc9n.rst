.. mchoice:: mc9n
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: ListMethods
   :topics: Lists/ListMethods
   :from_source: None
   :answer_a: [4, 2, 8, 6, 5, False, True]
   :answer_b: [4, 2, 8, 6, 5, True, False]
   :answer_c: [True, False, 4, 2, 8, 6, 5]
   :correct: b
   :feedback_a: True was added first, then False was added last.
   :feedback_b: Yes, each item is added to the end of the list.
   :feedback_c: append adds at the end, not the beginning.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     alist.append(True)
     alist.append(False)
     print(alist)