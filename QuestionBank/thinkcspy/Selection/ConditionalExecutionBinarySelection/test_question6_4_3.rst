.. mchoice:: test_question6_4_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: ConditionalExecutionBinarySelection
   :topics: Selection/ConditionalExecutionBinarySelection
   :from_source: T
   :practice: T
   :answer_a: Output a
   :answer_b: Output b
   :answer_c: Output c
   :answer_d: Output d
   :correct: c
   :feedback_a: Although TRUE is printed after the if-else statement completes, both blocks within the if-else statement print something too.  In this case, Python would have had to have skipped both blocks in the if-else statement, which it never would do.
   :feedback_b: Because there is a TRUE printed after the if-else statement ends, Python will always print TRUE as the last statement.
   :feedback_c: Python will print FALSE from within the else-block (because 5+4 does not equal 10), and then print TRUE after the if-else statement completes.
   :feedback_d: To print these three lines, Python would have to execute both blocks in the if-else statement, which it can never do.
   :pct_on_first: 0.8698500608
   :total_students_attempting: 14806
   :num_students_correct: 14760.0
   :mean_clicks_to_correct: 1.2054878049

   What does the following code print?
   
   .. code-block:: python
   
     if 4 + 5 == 10:
         print("TRUE")
     else:
         print("FALSE")
     print("TRUE")
   
   ::
   
      a. TRUE
   
      b.
         TRUE
         FALSE
   
      c.
         FALSE
         TRUE
      d.
         TRUE
         FALSE
         TRUE