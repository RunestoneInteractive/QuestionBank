.. mchoice:: test_question9_13_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: ListMethods
   :topics: Lists/ListMethods
   :from_source: T
   :practice: T
   :answer_a: [4, 2, 8, 6, 5, False, True]
   :answer_b: [4, 2, 8, 6, 5, True, False]
   :answer_c: [True, False, 4, 2, 8, 6, 5]
   :correct: b
   :feedback_a: True was added first, then False was added last.
   :feedback_b: Yes, each item is added to the end of the list.
   :feedback_c: append adds at the end, not the beginning.
   :pct_on_first: 0.859246644
   :total_students_attempting: 9982
   :num_students_correct: 9941.0
   :mean_clicks_to_correct: 1.1738255709

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4, 2, 8, 6, 5]
     alist.append(True)
     alist.append(False)
     print(alist)