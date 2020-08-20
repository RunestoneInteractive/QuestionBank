.. mchoice:: qtnt1_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: II only
   :answer_b: I only
   :answer_c: I and II only
   :answer_d: II and III only
   :answer_e: III only
   :correct: a
   :feedback_a: If an array is already sorted from smallest to largest then we do not need to move anything in the array and we would only need to go through each element at most once, so this is fastest run time for insertion sort.
   :feedback_b: An array in reverse order is actually the worst run time for insertion sort because we would need to move everything to make it in order from smallest to largest.
   :feedback_c: II is correct, but number I will actually be the worst run time for insertion sort since all values will have to be moved each time through the loop.
   :feedback_d: While II is the correct anwser, an array in random order will have average run time.
   :feedback_e: When the array is not sorted the run time will be average.

   In which of these cases will an ascending order (from smallest to largest) insertion sort have the fastest run time?

   .. code-block:: java

      I.   An array that is in reverse order (from largest to smallest).
      II.  An array that is in sorted order already (from smallest to largest).
      III. An array that is in random order (not already sorted).