.. mchoice:: question11_4_6
   :author: bmiller
   :difficulty: 3.0163710778
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: square
   :answer_b: g
   :answer_c: a number
   :correct: b
   :feedback_a: Before executing square, it has to figure out what value to pass in, so g is executed first
   :feedback_b: g has to be executed and return a value in order to know what paramater value to provide to x.
   :feedback_c: square and g both have to execute before the number is printed.
   :practice: T
   :pct_on_first: 0.4959072306
   :total_students_attempting: 1466
   :num_students_correct: 1455.0
   :mean_clicks_to_correct: 1.7243986254

   Which will print out first, square, g, or a number?
   
   .. code-block:: python
   
       def square(x):
           print("square")
           return x*x
   
       def g(y):
           print("g")
           return y + 3
   
       print(square(g(2)))