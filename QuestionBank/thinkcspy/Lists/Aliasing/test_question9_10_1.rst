.. mchoice:: test_question9_10_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Aliasing
   :topics: Lists/Aliasing
   :from_source: T
   :practice: T
   :answer_a: [4, 2, 8, 6, 5]
   :answer_b: [4, 2, 8, 999, 5]
   :correct: b
   :feedback_a: blist is not a copy of alist, it is a reference to the list alist refers to.
   :feedback_b: Yes, since alist and blist both reference the same list, changes to one also change the other.
   :pct_on_first: 0.7323943662
   :total_students_attempting: 10224
   :num_students_correct: 10144.0
   :mean_clicks_to_correct: 1.2793769716

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4, 2, 8, 6, 5]
     blist = alist
     blist[3] = 999
     print(alist)