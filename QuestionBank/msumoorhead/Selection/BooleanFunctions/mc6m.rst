.. mchoice:: mc6m
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Selection
   :subchapter: BooleanFunctions
   :topics: Selection/BooleanFunctions
   :from_source: None
   :answer_a: Yes
   :answer_b: No
   :correct: a
   :feedback_a: It is perfectly valid to return the result of evaluating a Boolean expression.
   :feedback_b: x +y < z is a valid Boolean expression, which will evaluate to True or False.  It is perfectly legal to return True or False from a function, and to have the statement to be evaluated in the same line as the return keyword.

   Is the following statement legal in Python (assuming x, y and z are defined to be numbers)?

   .. code-block:: python

     return x + y < z