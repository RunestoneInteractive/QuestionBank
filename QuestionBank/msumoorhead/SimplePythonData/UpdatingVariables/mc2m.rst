.. mchoice:: mc2m
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: SimplePythonData
   :subchapter: UpdatingVariables
   :topics: SimplePythonData/UpdatingVariables
   :from_source: None
   :answer_a: 12
   :answer_b: -1
   :answer_c: 11
   :answer_d: Nothing.  An error occurs because x can never be equal to x - 1.
   :correct: c
   :feedback_a: The value of x changes in the second statement.
   :feedback_b: In the second statement, substitute the current value of x before subtracting 1.
   :feedback_c: Yes, this statement sets the value of x equal to the current value minus 1.
   :feedback_d: Remember that variables in Python are different from variables in math in that they (temporarily) hold values, but can be reassigned.


   What is printed when the following statements execute?

   .. code-block:: python

     x = 12
     x = x - 1
     print(x)