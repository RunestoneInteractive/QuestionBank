.. mchoice:: question11_4_4
   :author: bmiller
   :difficulty: 1.9966510382
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: 8
   :answer_b: 16
   :answer_c: Error: can't put a function invocation inside parentheses
   :correct: b
   :feedback_a: It squares 2, yielding the value 4. But that doesn't mean the next value multiplies 2 and 4.
   :feedback_b: It squares 2, yielding the value 4. 4 is then passed as a value to square again, yeilding 16.
   :feedback_c: This is a more complicated expression, but still valid. The expression square(2) is evaluated, and the return value 4 substitutes for square(2) in the expression.
   :pct_on_first: 0.7508372405
   :total_students_attempting: 1493
   :num_students_correct: 1484.0
   :mean_clicks_to_correct: 1.3221024259

   What will the following code output?
   
   .. code-block:: python
   
       def square(x):
           y = x * x
           return y
   
       print(square(square(2)))