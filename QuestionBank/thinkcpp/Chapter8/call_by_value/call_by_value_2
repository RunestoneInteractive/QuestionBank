.. mchoice:: call_by_value_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: call_by_value
   :topics: Chapter8/call_by_value
   :from_source: T
   :practice: T
   :answer_a: 6.0, 8.0, 3.0, 4.0
   :answer_b: 6.0, 8.0, 6.0, 8.0
   :answer_c: 6.08.03.04.0
   :answer_d: 6.08.06.08.0
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Remember the rules of pass by value.
   :feedback_c: Take a look at exactly what is being outputted.
   :feedback_d: Take a look at exactly what is being outputted.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   What will print?
   
   .. code-block:: cpp
   
      struct Point {
        double x, y;
      };
   
      void timesTwo (Point p) {
        cout << "(" << p.x * 2 << ", " << p.y * 2 << ")";
      }
   
      int main() {
        Point blank = { 3.0, 4.0 };
        timesTwo (blank);
        cout << ", " << blank << endl;
      }