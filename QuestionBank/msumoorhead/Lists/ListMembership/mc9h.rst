.. mchoice:: mc9h
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: ListMembership
   :topics: Lists/ListMembership
   :from_source: None
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: in returns True for top level items only.  57 is in a sublist.
   :feedback_b: Yes, 57 is not a top level item in alist.  It is in a sublist.

   What is printed by the following statements?

   .. code-block:: python

     alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
     print(57 in alist)