.. mchoice:: mc9w
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: AppendversusConcatenate
   :topics: Lists/AppendversusConcatenate
   :from_source: None
   :answer_a: [4, 2, 8, 6, 5, 999]
   :answer_b: Error, you cannot concatenate a list with an integer.
   :correct: b
   :feedback_a: You cannot concatenate a list with an integer.
   :feedback_b: Yes, in order to perform concatenation you would need to write alist+[999].  You must have two lists.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     alist = alist + 999
     print(alist)