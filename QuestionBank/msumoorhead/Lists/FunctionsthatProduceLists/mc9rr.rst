.. mchoice:: mc9rr
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: FunctionsthatProduceLists
   :topics: Lists/FunctionsthatProduceLists
   :from_source: None
   :answer_a: [4, 2, 8, 6, 5]
   :answer_b: [4, 2, 8, 6, 5, 5]
   :answer_c: [9, 7, 13, 11, 10]
   :answer_d: Error, you cannot concatenate inside an append.
   :correct: c
   :feedback_a: 5 is added to each item before the append is peformed.
   :feedback_b: There are too many items in this list.  Only 5 append operations are performed.
   :feedback_c: Yes, the for loop processes each item of the list.  5 is added before it is appended to blist.
   :feedback_d: 5 is added to each item before the append is performed.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4, 2, 8, 6, 5]
     blist = [ ]
     for item in alist:
         blist.append(item+5)
     print(blist)