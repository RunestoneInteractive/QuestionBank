.. mchoice:: mc6i
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Selection
   :subchapter: Nestedconditionals
   :topics: Selection/Nestedconditionals
   :from_source: None
   :answer_a: No
   :answer_b: Yes
   :correct: a
   :feedback_a: This is a legal nested if-else statement.  The inner if-else statement is contained completely within the body of the outer else-block.
   :feedback_b: This is a legal nested if-else statement.  The inner if-else statement is contained completely within the body of the outer else-block.

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