.. mchoice:: question11_3_4
   :author: bmiller
   :difficulty: 3.9201030928
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionParameters
   :topics: Functions/FunctionParameters
   :from_source: T
   :answer_a: print_many(x, y)
   :answer_b: print_many
   :answer_c: print_many("Greetings")
   :answer_d: print_many("Greetings", 10):
   :answer_e: print_many("Greetings", z)
   :correct: e
   :feedback_a: No, x and y are the names of the formal parameters to this function.  When the function is called, it requires actual values to be passed in.
   :feedback_b: A function call always requires parentheses after the name of the function.
   :feedback_c: This function takes two parameters (arguments)
   :feedback_d: A colon is only required in a function definition.  It will cause an error with a function call.
   :feedback_e: Since z has the value 3, we have passed in two correct values for this function. "Greetings" will be printed 3 times.
   :pct_on_first: 0.2699742268
   :total_students_attempting: 1552
   :num_students_correct: 1544.0
   :mean_clicks_to_correct: 2.3601036269

   Considering the function below, which of the following statements correctly invokes, or calls, this function (i.e., causes it to run)?
   
   .. code-block:: python
   
      def print_many(x, y):
         """Print out string x, y times."""
         for i in range(y):
             print(x)
   
      z = 3