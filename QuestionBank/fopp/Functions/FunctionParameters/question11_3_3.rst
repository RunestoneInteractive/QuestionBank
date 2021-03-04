.. mchoice:: question11_3_3
   :author: bmiller
   :difficulty: 1.4723809524
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionParameters
   :topics: Functions/FunctionParameters
   :from_source: T
   :answer_a: i
   :answer_b: x
   :answer_c: x, y
   :answer_d: x, y, i
   :correct: c
   :feedback_a: i is a variable used inside of the function, but not a parameter, which is passed in to the function.
   :feedback_b: x is only one of the parameters to this function.
   :feedback_c: Yes, the function specifies two parameters: x and y.
   :feedback_d: the parameters include only those variables whose values that the function expects to receive as input. They are specified in the header of the function.
   :pct_on_first: 0.8819047619
   :total_students_attempting: 1575
   :num_students_correct: 1569.0
   :mean_clicks_to_correct: 1.184193754

   What are the parameters of the following function?
   
   .. code-block:: python
   
     def print_many(x, y):
         """Print out string x, y times."""
         for i in range(y):
             print(x)