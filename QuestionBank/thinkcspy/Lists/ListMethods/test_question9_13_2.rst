.. mchoice:: test_question9_13_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: ListMethods
   :topics: Lists/ListMethods
   :from_source: T
   :practice: T
   :answer_a: [False, 4, 2, True, 8, 6, 5]
   :answer_b: [4, False, True, 2, 8, 6, 5]
   :answer_c: [False, 2, True, 6, 5]
   :correct: a
   :feedback_a: Yes, first True was added at index 2, then False was added at index 0.
   :feedback_b: insert will place items at the index position specified and move everything down to the right.
   :feedback_c: insert does not remove anything or replace anything.
   :pct_on_first: 0.574448807
   :total_students_attempting: 9933
   :num_students_correct: 9880.0
   :mean_clicks_to_correct: 1.5665991903

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [4, 2, 8, 6, 5]
     alist.insert(2, True)
     alist.insert(0, False)
     print(alist)