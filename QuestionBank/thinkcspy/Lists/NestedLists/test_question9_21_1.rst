.. mchoice:: test_question9_21_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: NestedLists
   :topics: Lists/NestedLists
   :from_source: T
   :practice: T
   :answer_a: 6
   :answer_b: 8
   :answer_c: 888
   :answer_d: 999
   :correct: c
   :feedback_a: 6 is in the wrong list.  alist[1] refers to the second item in alist, namely [888,999].
   :feedback_b: 8 is in the wrong list.  alist[1] refers to the second item in alist, namely [888,999].
   :feedback_c: Yes, alist[0][1][0] is True and alist[1] is the second list, the first item is 888.
   :feedback_d: alist[0][1][0] is True.  Take another look at the if statement.
   :pct_on_first: 0.6620872499
   :total_students_attempting: 8298
   :num_students_correct: 8238.0
   :mean_clicks_to_correct: 1.5235494052

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [ [4, [True, False], 6, 8], [888, 999] ]
     if alist[0][1][0]:
        print(alist[1][0])
     else:
        print(alist[1][1])