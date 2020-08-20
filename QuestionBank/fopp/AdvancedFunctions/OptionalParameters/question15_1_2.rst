.. mchoice:: question15_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: OptionalParameters
   :topics: AdvancedFunctions/OptionalParameters
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: None
   :answer_d: Runtime error since the second parameter value is missing.
   :correct: b
   :feedback_a: Since one parameter value is specified, it is bound to x; y gets the default value of 1.
   :feedback_b: Since one parameter value is specified, it is bound to x; y gets the default value of 1.
   :feedback_c: The function does return a value.
   :feedback_d: Because both parameters have default values specified in the definition, they are both optional.
   :practice: T
   :pct_on_first: 0.7927710843
   :total_students_attempting: 415
   :num_students_correct: 412.0
   :mean_clicks_to_correct: 1.2936893204

   What will the following code print?
   
   .. code-block:: python
   
       def f(x = 0, y = 1):
           return x * y
   
       print(f(1))