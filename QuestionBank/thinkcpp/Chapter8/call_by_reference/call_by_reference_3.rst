.. mchoice:: call_by_reference_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: call_by_reference
   :topics: Chapter8/call_by_reference
   :from_source: T
   :practice: T
   :answer_a: 2 4
   :answer_b: 2 4 2
   :answer_c: 4 4 2
   :answer_d: 2 4 4
   :correct: d
   :feedback_a: Take a look at exactly what is being outputted.
   :feedback_b: Remember the rules of pass by reference.
   :feedback_c: Take a look at exactly what is being outputted.
   :feedback_d: Correct!
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   What will print?
   
   .. code-block:: cpp
   
      int addTwo(int& x) {
        cout << x << " ";
        x = x + 2;
        cout << x << " ";
        return x;
      }
   
      int main() {
        int num = 2;
        addTwo(num);
        cout << num << endl;
      }