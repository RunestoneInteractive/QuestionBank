.. mchoice:: mc2k
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: None
   :answer_a: 192
   :answer_b: 256
   :answer_c: 12
   :answer_d: 768
   :correct: d
   :feedback_a: Exponentiation (**) is processed right to left, so take 2 ** 3 first.
   :feedback_b: Remember to multiply by 3.
   :feedback_c: There are two exponentiations.
   :feedback_d: Exponentiation has precedence over multiplication, but its precedence goes from right to left!  So 2 ** 3 is 8, 2 ** 8 is 256 and 256 * 3 is 768.

   What is the value of the following expression:

   .. code-block:: python

      2 ** 2 ** 3 * 3