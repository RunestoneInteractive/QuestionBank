.. mchoice:: question15_1_1
   :author: bmiller
   :difficulty: 1.7238095238
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: OptionalParameters
   :topics: AdvancedFunctions/OptionalParameters
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: None
   :answer_d: Runtime error since no parameters are passed in the call to f.
   :correct: a
   :feedback_a: Since no parameters are specified, x is 0 and y is 1, so 0 is returned.
   :feedback_b: 0 * 1 is 0.
   :feedback_c: The function does return a value.
   :feedback_d: Because both parameters have default values specified in the definition, they are both optional.
   :practice: T
   :pct_on_first: 0.819047619
   :total_students_attempting: 420
   :num_students_correct: 418.0
   :mean_clicks_to_correct: 1.2511961722

   What will the following code print?
   
   .. code-block:: python
   
       def f(x = 0, y = 1):
           return x * y
   
       print(f())