.. mchoice:: test_question5_1_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: functions
   :topics: Functions/functions
   :from_source: T
   :practice: T
   :answer_a: i
   :answer_b: t
   :answer_c: t, sz
   :answer_d: t, sz, i
   :correct: c
   :feedback_a: i is a variable used inside of the function, but not a parameter, which is passed in to the function.
   :feedback_b: t is only one of the parameters to this function.
   :feedback_c: Yes, the function specifies two parameters: t and sz.
   :feedback_d: the parameters include only those variables whose values that the function expects to receive as input.  They are specified in the header of the function.
   :pct_on_first: 0.8977237678
   :total_students_attempting: 16211
   :num_students_correct: 16178.0
   :mean_clicks_to_correct: 1.1516874768

   What are the parameters of the following function?
   
   .. code-block:: python
   
     def drawSquare(t, sz):
         """Make turtle t draw a square of with side sz."""
         for i in range(4):
             t.forward(sz)
             t.left(90)