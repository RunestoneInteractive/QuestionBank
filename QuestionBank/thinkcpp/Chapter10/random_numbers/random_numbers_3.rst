.. mchoice:: random_numbers_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: random_numbers
   :topics: Chapter10/random_numbers
   :from_source: T
   :answer_a: int y = x / 12
   :answer_b: int y = x % 12
   :answer_c: int y = x / 13
   :answer_d: int y = x % 13
   :correct: d
   :feedback_a: Incorrect! This returns some random number between 0 and x / 12, which is out of range.
   :feedback_b: Incorrect! This returns a random number between 0 and 11.
   :feedback_c: Incorrect! This returns some random number between 0 and x / 13, which is out of range.
   :feedback_d: Correct!
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   If we wanted to generate a random number between 0 and 12, and we have previously declared int ``int x = random ();``, what should be our next line of code?