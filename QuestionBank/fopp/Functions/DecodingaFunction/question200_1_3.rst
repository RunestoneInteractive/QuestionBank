.. mchoice:: question200_1_3
   :author: bmiller
   :difficulty: 3.4706755754
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
   :correct: c
   :feedback_a: append can't be performed on integers.
   :feedback_b: append can't be performed on floats.
   :feedback_c: append can be performed on lists.
   :feedback_d: append can't be performed on strings.
   :feedback_e: You can tell from some of the operations that are performed on it.
   :practice: T
   :pct_on_first: 0.3823311062
   :total_students_attempting: 1347
   :num_students_correct: 1329.0
   :mean_clicks_to_correct: 2.5214446953

   What are the possible types of variable z?
   
   .. code-block:: python
   
      def cyu3(x, y, z):
         if x - y > 0:
            return y -2
         else:
            z.append(y)
            return x + 3