.. mchoice:: question11_11_1
   :author: bmiller
   :difficulty: 2.2686804452
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Printvsreturn
   :topics: Functions/Printvsreturn
   :from_source: T
   :answer_a: 2
   :answer_b: 5
   :answer_c: 7
   :answer_d: 25
   :answer_e: Error: y has a value but x is an unbound variable inside the square function
   :correct: c
   :feedback_a: 2 is the input; the value returned from h is what will be printed.
   :feedback_b: Don't forget that 2 gets squared.
   :feedback_c: First square 2, then add 3.
   :feedback_d: 3 is added to the result of squaring 2
   :feedback_e: When square is called, x is bound to the parameter value that is passed in, 2.
   :practice: T
   :pct_on_first: 0.6828298887
   :total_students_attempting: 1258
   :num_students_correct: 1241.0
   :mean_clicks_to_correct: 1.5761482675

   What will the following code output?
   
   .. code-block:: python
   
       def square(x):
           return x*x
   
       def g(y):
           return y + 3
   
       def h(y):
           return square(y) + 3
   
       print(h(2))