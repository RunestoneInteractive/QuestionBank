.. mchoice:: test_question9_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: ListMembership
   :topics: Lists/ListMembership
   :from_source: T
   :practice: T
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: in returns True for top level items only.  57 is in a sublist.
   :feedback_b: Yes, 57 is not a top level item in alist.  It is in a sublist.
   :pct_on_first: 0.7161300734
   :total_students_attempting: 12393
   :num_students_correct: 12227.0
   :mean_clicks_to_correct: 1.2891142553

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
     print(57 in alist)