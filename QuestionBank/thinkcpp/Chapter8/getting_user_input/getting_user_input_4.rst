.. mchoice:: getting_user_input_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: getting_user_input
   :topics: Chapter8/getting_user_input
   :from_source: T
   :practice: T
   :answer_a: John
   :answer_b: J
   :answer_c: John Doe
   :correct: c
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Correct!
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   The user types in ``John Doe``. What prints?
   
   .. code-block:: cpp
   
      int main() {
        string name;
        cout << "What is your name? ";
        getline (cin, name);
        cout << name << endl;
      }