.. mchoice:: question11_4_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: 25
   :answer_b: 50
   :answer_c: 25 + 25
   :correct: b
   :feedback_a: It squares 5 twice, and adds them together.
   :feedback_b: The two return values are added together.
   :feedback_c: The two results are substituted into the expression and then it is evaluated. The returned values are integers in this case, not strings.
   :practice: T
   :pct_on_first: 0.6946666667
   :total_students_attempting: 1500
   :num_students_correct: 1493.0
   :mean_clicks_to_correct: 1.3998660415

   What will the following code output?
   
   .. code-block:: python
   
       def square(x):
           y = x * x
           return y
   
       print(square(5) + square(5))