.. mchoice:: test_question2_8_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: T
   :practice: T
   :answer_a: 768
   :answer_b: 128
   :answer_c: 12
   :answer_d: 256
   :correct: a
   :feedback_a: Exponentiation has precedence over multiplication, but its precedence goes from right to left!  So 2 ** 3 is 8, 2 ** 8 is 256 and 256 * 3 is 768.
   :feedback_b: Exponentiation (**) is processed right to left, so take 2 ** 3 first.
   :feedback_c: There are two exponentiations.
   :feedback_d: Remember to multiply by 3.
   :pct_on_first: 0.6662395596
   :total_students_attempting: 21072
   :num_students_correct: 20977.0
   :mean_clicks_to_correct: 1.6065690995

   What is the value of the following expression:
   
   .. code-block:: python
   
      2 ** 2 ** 3 * 3