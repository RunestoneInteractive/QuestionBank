.. mchoice:: qtnt4_16
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: x % y == 0
   :answer_b: x % y == 1
   :answer_c: x % y == 2
   :answer_d: x / y == 1
   :answer_e: x / y == 0
   :correct: a
   :feedback_a: The modulus operator (%) returns the remainder left by integer division. If x % y == 0, x is evenly divisible by y, leaving no remainder.
   :feedback_b: The modulus operator (%) returns the remainder left by integer division. If x % y == 1, x is not evenly divisible by y, as there is a remainder of 1 left over.
   :feedback_c: The modulus operator (%) returns the remainder left by integer division. If x % y == 2, x is not evenly divisible by y, because there is a remainder of 2 left after the division.
   :feedback_d: The modulus operator (%) is used to check if numbers are divisible by each other. The division operator (/) should be replaced with a %.
   :feedback_e: The division operator does not check if one number is divisible by another. In integer division, remainders are calculated by the modulus operator (%).


   The method ``divisible`` is shown below. In order for ``divisible`` to compile and run as intended, the method must return true if x is evenly divisible by y with no remainder, returning false otherwise. Which of the following could replace ``/* to be completed */`` to make the code work as intended?

   .. code-block:: java


     /* Precondition: x and y are both integers greater than 0 */
      public boolean divisible (int x, int y)
      {
          if ( /* to be completed */)
              return true;

          return false;
      }