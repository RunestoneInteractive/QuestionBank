.. mchoice:: test_question6_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: OmittingtheelseClauseUnarySelection
   :topics: Selection/OmittingtheelseClauseUnarySelection
   :from_source: T
   :practice: T
   :answer_a: Output a
   :answer_b: Output b
   :answer_c: Output c
   :answer_d: It will cause an error because every if must have an else clause.
   :correct: b
   :feedback_a: Because -10 is less than 0, Python will execute the body of the if-statement here.
   :feedback_b: Python executes the body of the if-block as well as the statement that follows the if-block.
   :feedback_c: Python will also execute the statement that follows the if-block (because it is not enclosed in an else-block, but rather just a normal statement).
   :feedback_d: It is valid to have an if-block without a corresponding else-block (though you cannot have an else-block without a corresponding if-block).
   :pct_on_first: 0.8231480204
   :total_students_attempting: 14498
   :num_students_correct: 14449.0
   :mean_clicks_to_correct: 1.263962904

   What does the following code print?
   
   .. code-block:: python
   
     x = -10
     if x < 0:
         print("The negative number ",  x, " is not valid here.")
     print("This is always printed")
   
   ::
   
     a.
     This is always printed
   
     b.
     The negative number -10 is not valid here
     This is always printed
   
     c.
     The negative number -10 is not valid here