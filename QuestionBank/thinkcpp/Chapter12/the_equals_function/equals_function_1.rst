.. mchoice:: equals_function_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter12
   :subchapter: the_equals_function
   :topics: Chapter12/the_equals_function
   :from_source: T
   :answer_a: Directly, using the build in == operator.
   :answer_b: Compare their ranks and suits separately using the == operator. If either comparison is true, then they are equal.
   :answer_c: Compare their ranks and suits separately using the == operator. If either comparison is false, then they are NOT equal.
   :answer_d: They cannot be compared because they are non-numerical objects.
   :correct: c
   :feedback_a: Incorrect! We have to create our own method to compare two Card objects, the == operator won't work.
   :feedback_b: Incorrect! This would return true if two cards have the same rank, but different suits OR the same suit, but different ranks.
   :feedback_c: Correct! Both ranks and suits must be the same for two cards to be equal.
   :feedback_d: Incorrect! Card objects can be compared, but we must create our own method.

   How can we compare two ``Card`` objects?