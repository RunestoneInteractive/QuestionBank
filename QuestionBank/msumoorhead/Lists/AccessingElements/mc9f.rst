.. mchoice:: mc9f
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: AccessingElements
   :topics: Lists/AccessingElements
   :from_source: None
   :answer_a: 56
   :answer_b: c
   :answer_c: cat
   :answer_d: Error, you cannot have two index values unless you are using slicing.
   :correct: b
   :feedback_a: Indexes start with 0, not 1.
   :feedback_b: Yes, the first character of the string at index 2 is c
   :feedback_c: cat is the item at index 2 but then we index into it further.
   :feedback_d: Using more than one index is fine.  You read it from left to right.

   What is printed by the following statements?

   .. code-block:: python

     alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
     print(alist[2][0])