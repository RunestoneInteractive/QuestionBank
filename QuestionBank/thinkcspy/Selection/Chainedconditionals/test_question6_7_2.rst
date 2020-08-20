.. mchoice:: test_question6_7_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Chainedconditionals
   :topics: Selection/Chainedconditionals
   :from_source: T
   :practice: T
   :answer_a: a
   :answer_b: b
   :answer_c: c
   :correct: c
   :feedback_a: While the value in x is less than the value in y (3 is less than 5) it is not less than the value in z (3 is not less than 2).
   :feedback_b: The value in y is not less than the value in x (5 is not less than 3).
   :feedback_c: Since the first two Boolean expressions are false the else will be executed.
   :pct_on_first: 0.7771466509
   :total_students_attempting: 13556
   :num_students_correct: 13503.0
   :mean_clicks_to_correct: 1.3071909946

   What will the following code print if x = 3, y = 5, and z = 2?
   
   .. code-block:: python
   
     if x < y and x < z:
         print("a")
     elif y < x and y < z:
         print("b")
     else:
         print("c")