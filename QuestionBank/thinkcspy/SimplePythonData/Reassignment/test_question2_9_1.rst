.. mchoice:: test_question2_9_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Reassignment
   :topics: SimplePythonData/Reassignment
   :from_source: T
   :practice: T
   :answer_a: x is 15 and y is 15
   :answer_b: x is 22 and y is 22
   :answer_c: x is 15 and y is 22
   :answer_d: x is 22 and y is 15
   :correct: d
   :feedback_a: Look at the last assignment statement which gives x a different value.
   :feedback_b: No, x and y are two separate variables.  Just because x changes in the last assignment statement, it does not change the value that was copied into y in the second statement.
   :feedback_c: Look at the last assignment statement, which reassigns x, and not y.
   :feedback_d: Yes, x has the value 22 and y the value 15.
   :pct_on_first: 0.7181584705
   :total_students_attempting: 21026
   :num_students_correct: 20940.0
   :mean_clicks_to_correct: 1.5981375358

   
   After the following statements, what are the values of x and y?
   
   .. code-block:: python
   
     x = 15
     y = x
     x = 22