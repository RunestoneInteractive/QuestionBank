.. mchoice:: question200_1_2
   :author: bmiller
   :difficulty: 3.0382352941
   :basecourse: fopp
   :chapter: Functions
   :subchapter: DecodingaFunction
   :topics: Functions/DecodingaFunction
   :from_source: T
   :multiple_answers: 
   :answer_a: integer
   :answer_b: float
   :answer_c: list
   :answer_d: string
   :answer_e: Can't tell
   :correct: a,b
   :feedback_a: x - y, y-2, and x+3 can all be performed on integers.
   :feedback_b: x - y, y-2, and x+3 can all be performed on floats.
   :feedback_c: x - y, y-2, and x+3 can't be performed on lists.
   :feedback_d: x - y and y-2 can't be performed on strings.
   :feedback_e: You can tell from some of the operations that are performed on them.
   :practice: T
   :pct_on_first: 0.4904411765
   :total_students_attempting: 1360
   :num_students_correct: 1342.0
   :mean_clicks_to_correct: 2.2280178838

   What are the possible types of variables x and y?
   
   .. code-block:: python
   
      def cyu3(x, y, z):
         if x - y > 0:
            return y -2
         else:
            z.append(y)
            return x + 3