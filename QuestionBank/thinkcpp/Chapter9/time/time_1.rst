.. mchoice:: time_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: time
   :topics: Chapter9/time
   :from_source: T
   :answer_a: sandwich, coffee, pastry
   :answer_b: dollar, cents
   :answer_c: Price, struct
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Try again.
   :feedback_c: Try again.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Which of the following words are variables of type ``Price``?
   
   .. code-block:: cpp
   
      struct Price {
        int dollar, cents;
      };
   
      int main() {
        Price sandwich = { 3, 45 };
        Price coffee = { 2, 50 };
        Price pastry = { 2, 0 };
      }