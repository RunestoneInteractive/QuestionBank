.. mchoice:: mc2n
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: SimplePythonData
   :subchapter: UpdatingVariables
   :topics: SimplePythonData/UpdatingVariables
   :from_source: None
   :answer_a: 12
   :answer_b: 9
   :answer_c: 15
   :answer_d: Nothing.  An error occurs because x cannot be used that many times in assignment statements.
   :correct: c
   :feedback_a: The value of x changes in the second statement.
   :feedback_b: Each statement changes the value of x, so 9 is not the final result.
   :feedback_c: Yes, starting with 12, subtract 3, than add 5, and finally add 1.
   :feedback_d: Remember that variables in Python are different from variables in math in that they (temporarily) hold values, but can be reassigned.


   What is printed when the following statements execute?

   .. code-block:: python

     x = 12
     x = x - 3
     x = x + 5
     x = x + 1
     print(x)