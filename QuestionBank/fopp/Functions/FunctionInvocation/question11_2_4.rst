.. mchoice:: question11_2_4
   :author: bmiller
   :difficulty: 2.3583021223
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FunctionInvocation
   :topics: Functions/FunctionInvocation
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 3
   :answer_d: 4
   :answer_e: 7
   :correct: e
   :feedback_a: Here the the function is invoked and there is also a separate print statement.
   :feedback_b: There is only one print statement outside the funciton, but the invocations of hello also cause lines to print.
   :feedback_c: There are three print statements, but the function is invoked more than once.
   :feedback_d: Each time the function is invoked, it will print two lines, not one.
   :feedback_e: Three invocations generate two lines each, plus the line "It works".
   :practice: T
   :pct_on_first: 0.6604244694
   :total_students_attempting: 1602
   :num_students_correct: 1593.0
   :mean_clicks_to_correct: 1.842435656

   How many lines will be output by executing this code?
   
   .. code-block:: python
   
      def hello():
         print("Hello")
         print("Glad to meet you")
   
      hello()
      print("It works")
      hello()
      hello()