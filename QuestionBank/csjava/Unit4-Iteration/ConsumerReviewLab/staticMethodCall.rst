.. mchoice:: staticMethodCall
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: ConsumerReviewLab
   :topics: Unit4-Iteration/ConsumerReviewLab
   :from_source: T
   :answer_a: double value = sentimentVal();
   :answer_b: sentimentVal("terrible");
   :answer_c: word.sentimentVal("terrible");
   :answer_d: double value = Review.sentimentVal("terrible");
   :answer_e: int value = sentimentVal("terrible");
   :correct: d
   :feedback_a: sentimentVal takes a String argument and is in the class Review.
   :feedback_b: sentimentVal returns a value and is in the class Review.
   :feedback_c: sentimentVal returns a value and is a static method in the class Review.
   :feedback_d: That's right1 sentimentVal takes a String argument and returns a double value and is a static method that can be called with the class name Review.
   :feedback_e: sentimentVal returns a double value, not int, and it's a static method in the class Review.


   Which of the following correctly calls the method sentimentVal?