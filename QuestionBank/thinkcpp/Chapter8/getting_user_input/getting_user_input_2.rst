.. mchoice:: getting_user_input_2
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
   :correct: b
   :feedback_a: Try again! Pay attention to the data type of name.
   :feedback_b: Correct!
   :feedback_c: Try again!
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.5

   The user types in ``John Doe``. What prints?
   
   .. code-block:: cpp
   
      int main() {
        char name;
        cout << "What is your name? ";
        cin >> name;
        cout << name << endl;
      }