.. mchoice:: mc9t
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: Aliasing
   :topics: Lists/Aliasing
   :from_source: None
   :answer_a: [4, 2, 8, 6, 5]
   :answer_b: [4, 2, 8, 999, 5]
   :correct: b
   :feedback_a: blist is not a copy of alist, it is a reference to the list alist refers to.
   :feedback_b: Yes, since alist and blist both reference the same list, changes to one also change the other.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     blist = alist
     blist[3] = 999
     print(alist)