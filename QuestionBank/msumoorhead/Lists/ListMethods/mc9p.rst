.. mchoice:: mc9p
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: ListMethods
   :topics: Lists/ListMethods
   :from_source: None
   :answer_a: [4, 8, 6]
   :answer_b: [2, 6, 5]
   :answer_c: [4, 2, 6]
   :correct: c
   :feedback_a: pop(2) removes the item at index 2, not the 2 itself.
   :feedback_b: pop() removes the last item, not the first.
   :feedback_c: Yes, first the 8 was removed, then the last item, which was 5.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     temp = alist.pop(2)
     temp = alist.pop()
     print(alist)