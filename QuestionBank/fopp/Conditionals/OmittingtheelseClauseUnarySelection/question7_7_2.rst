.. mchoice:: question7_7_2
   :author: bmiller
   :difficulty: 2.4069898534
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: OmittingtheelseClauseUnarySelection
   :topics: Conditionals/OmittingtheelseClauseUnarySelection
   :from_source: T
   :answer_a: No
   :answer_b: Yes
   :correct: b
   :feedback_a: Every else-block must have exactly one corresponding if-block.  If you want to chain if-else statements together, you must use the else if construct, described in the chained conditionals section.
   :feedback_b: This will cause an error because the second else-block is not attached to a corresponding if-block.
   :practice: T
   :pct_on_first: 0.6482525366
   :total_students_attempting: 1774
   :num_students_correct: 1753.0
   :mean_clicks_to_correct: 1.358243012

   Will the following code cause an error?
   
   .. code-block:: python
   
     x = -10
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     else:
         print(x, " is a positive number")
     else:
         print("This is always printed")