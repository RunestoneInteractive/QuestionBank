.. mchoice:: test_question8_3_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: StringMethods
   :topics: Strings/StringMethods
   :from_source: T
   :practice: T
   :answer_a: Nothing - it causes an error
   :answer_b: sum of {} and {} is {}; product: {}. 2 6 8 12
   :answer_c: sum of 2 and 6 is 8; product: 12.
   :answer_d: sum of {2} and {6} is {8}; product: {12}.
   :correct: c
   :feedback_a: It is legal format syntax:  put the data in place of the braces.
   :feedback_b: Put the data into the format string; not after it.
   :feedback_c: Yes, correct substitutions!
   :feedback_d: Close:  REPLACE the braces.
   :pct_on_first: 0.6973383335
   :total_students_attempting: 10933
   :num_students_correct: 10876.0
   :mean_clicks_to_correct: 1.4396837072

   
   What is printed by the following statements?
   
   .. code-block:: python
   
       x = 2
       y = 6
       print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))