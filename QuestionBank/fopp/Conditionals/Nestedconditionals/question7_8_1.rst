.. mchoice:: question7_8_1
   :author: bmiller
   :difficulty: 1.7600721587
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Nestedconditionals
   :topics: Conditionals/Nestedconditionals
   :from_source: T
   :answer_a: No
   :answer_b: Yes
   :correct: a
   :feedback_a: This is a legal nested if-else statement.  The inner if-else statement is contained completely within the body of the outer else-block.
   :feedback_b: This is a legal nested if-else statement.  The inner if-else statement is contained completely within the body of the outer else-block.
   :practice: T
   :pct_on_first: 0.8099819603
   :total_students_attempting: 1663
   :num_students_correct: 1656.0
   :mean_clicks_to_correct: 1.1956521739

   Will the following code cause an error?
   
   .. code-block:: python
   
     x = -10
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     else:
         if x > 0:
             print(x, " is a positive number")
         else:
             print(x," is 0")