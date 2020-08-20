.. mchoice:: test_question9_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: AccessingElements
   :topics: Lists/AccessingElements
   :from_source: T
   :practice: T
   :answer_a: Error, you cannot use the upper method on a list.
   :answer_b: 2
   :answer_c: CAT
   :correct: c
   :feedback_a: alist[2] is the string cat so the upper method is legal
   :feedback_b: 2 is the index.  We want the item at that index.
   :feedback_c: Yes, the string cat is upper cased to become CAT.
   :pct_on_first: 0.7588026782
   :total_students_attempting: 12695
   :num_students_correct: 12653.0
   :mean_clicks_to_correct: 1.2970046629

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
     print(alist[2].upper())