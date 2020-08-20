.. mchoice:: question11_10_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: FlowofExecutionSummary
   :topics: Functions/FlowofExecutionSummary
   :from_source: T
   :answer_a: 25
   :answer_b: 5
   :answer_c: 125
   :answer_d: 32
   :correct: a
   :feedback_a: The function square returns the square of its input (via a call to pow).
   :feedback_b: What is printed is the output of the square function.  5 is the input to the square function.
   :feedback_c: Notice that pow is called from within square with a base (b) of 5 and a power (p) of two.
   :feedback_d: Notice that pow is called from within square with a base (b) of 5 and a power (p) of two.
   :practice: T
   :pct_on_first: 0.7831223629
   :total_students_attempting: 1185
   :num_students_correct: 1171.0
   :mean_clicks_to_correct: 1.4278394535

   Consider the following Python code. Note that line numbers are included on the left.
   
   .. code-block:: python
      :linenos:
   
      def pow(b, p):
          y = b ** p
          return y
   
      def square(x):
          a = pow(x, 2)
          return a
   
      n = 5
      result = square(n)
      print(result)
   
   What does this function print?