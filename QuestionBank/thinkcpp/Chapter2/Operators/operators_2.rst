.. mchoice:: operators_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Operators
   :topics: Chapter2/Operators
   :from_source: F
   :answer_a: 0
   :answer_b: 1
   :answer_c: .667
   :answer_d: .6666666667
   :correct: a
   :feedback_a: Correct! In integer division, the decimal part is simply discarded, which is why the result would be 0.
   :feedback_b: The decimal part is discarded. This means we do not round up, only down.
   :feedback_c: In integer division, an integer must be the result.
   :feedback_d: In integer division, an integer must be the result.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   What is the output?
   
   ::
   
       int main () {
         int sum = 2 / 3;
         cout << sum;
       }