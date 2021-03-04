.. mchoice:: df_question200_1_3
   :author: bmiller
   :difficulty: 3.0180451128
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
   :feedback_a: y-2 or  x+3 could produce an integer.
   :feedback_b: y-2 or  x+3 could produce a float.
   :feedback_c: y-2 or  x+3 can't produce a list.
   :feedback_d: neither y-2 or  x+3 could produce a string.
   :feedback_e: You can tell from the expressions that follow the word return.
   :practice: T
   :pct_on_first: 0.4954887218
   :total_students_attempting: 1330
   :num_students_correct: 1305.0
   :mean_clicks_to_correct: 2.0528735632

   What are the possible types of the return value from cyu3?
   
   .. code-block:: python
   
      def cyu3(x, y, z):
         if x - y > 0:
            return y -2
         else:
            z.append(y)
            return x + 3