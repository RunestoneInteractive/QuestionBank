.. mchoice:: question11_3_2
   :author: bmiller
   :difficulty: 2.2779552716
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionParameters
   :topics: Functions/FunctionParameters
   :from_source: T
   :answer_a: def print_many(x, y):
   :answer_b: print_many
   :answer_c: print_many(x, y)
   :answer_d: Print out string x, y times.
   :correct: b
   :feedback_a: This line is the complete function header (except for the semi-colon) which includes the name as well as several other components.
   :feedback_b: Yes, the name of the function is given after the keyword def and before the list of parameters.
   :feedback_c: This includes the function name and its parameters
   :feedback_d: This is a comment stating what the function does.
   :pct_on_first: 0.6805111821
   :total_students_attempting: 1565
   :num_students_correct: 1560.0
   :mean_clicks_to_correct: 1.5730769231

   What is the name of the following function?
   
   .. code-block:: python
   
     def print_many(x, y):
         """Print out string x, y times."""
         for i in range(y):
             print(x)