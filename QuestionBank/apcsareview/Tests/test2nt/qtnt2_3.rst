.. mchoice:: qtnt2_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: 8
   :answer_b: 10
   :answer_c: 100
   :answer_d: 2000
   :answer_e: 11
   :correct: e
   :feedback_a: 2 ^ 8 = 256. There will not be enough passes to guarantee finding the value. Remember that binary search requires log2 (number of elements) passes to guarantee that a value will be found.
   :feedback_b: 2 ^ 10 = 1024. There will not be enough passes to guarantee finding the value. Remember that binary search requires log2 (number of elements) passes to guarantee that a value will be found.
   :feedback_c: The key will be found in 100 passes, but there is a better answer. Remember that binary search requires log2 (number of elements) passes to find a value.
   :feedback_d: With binary search, every element of the array does not have to be checked. Remember that although sequential search would require 2000 passes to guarantee the value was found, binary search requires log2 (number of elements) passes to find an object.
   :feedback_e: 2 ^ 11 = 2048. Because 2048 is larger than 2000, 11 passes will be more than enough to guarantee finding the value.

   A sorted array of integers containing 2000 elements is to be searched for ``key`` using a binary search method. Assuming ``key`` is in the array, what is the maximum number of iterations needed to find ``key``?