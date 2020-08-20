.. mchoice:: test_question6_7_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Chainedconditionals
   :topics: Selection/Chainedconditionals
   :from_source: T
   :practice: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: II and III
   :answer_e: I, II, and III
   :correct: b
   :feedback_a: You can not use a Boolean expression after an else.
   :feedback_b: Yes, II will give the same result.
   :feedback_c: No, III will not give the same result.  The first if statement will be true, but the second will be false, so the else part will execute.
   :feedback_d: No, Although II is correct III will not give the same result.  Try it.
   :feedback_e: No, in I you can not have a Boolean expression after an else.
   :pct_on_first: 0.4756115532
   :total_students_attempting: 13572
   :num_students_correct: 13461.0
   :mean_clicks_to_correct: 1.9997028453

   Which of I, II, and III below gives the same result as the following nested if?
   
   .. code-block:: python
   
     # nested if-else statement
     x = -10
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     else:
         if x > 0:
             print(x, " is a positive number")
         else:
             print(x, " is 0")
   
   
   .. code-block:: python
   
     I.
   
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     else x > 0:
         print(x, " is a positive number")
     else:
         print(x, " is 0")
   
   
   .. code-block:: python
   
     II.
   
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     elif x > 0:
         print(x, " is a positive number")
     else:
         print(x, " is 0")
   
   .. code-block:: python
   
     III.
   
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     if x > 0:
         print(x, " is a positive number")
     else:
         print(x, " is 0")