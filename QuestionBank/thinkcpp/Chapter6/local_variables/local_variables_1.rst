.. mchoice:: local_variables_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: local_variables
   :topics: Chapter6/local_variables
   :from_source: T
   :multiple_answers: 
   :answer_a: Yes, we cannot output the value of i outside of the for loop.
   :answer_b: Yes, we cannot output anything before the for loop.
   :answer_c: Yes, we cannot reassign i to 10 outside of the for loop.
   :answer_d: Yes, we cannot let i start at 1 in the for loop.
   :answer_e: No, there are no issues with the code below.
   :correct: a, c
   :feedback_a: The scope of i is restricted to the for loop, so we cannot change the value of i outside of the for loop.
   :feedback_b: This is allowed.
   :feedback_c: The scope of i is restricted to the for loop, so we cannot output the value of i outside of the for loop.
   :feedback_d: We are allowed to initialize i to any value.
   :feedback_e: There are issues with the code. Can you find them?
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 5.0

   Are there any issues with the code below?
   
   .. code-block:: cpp
   
    #include <iostream>
    using namespace std;
   
    int main() {
      cout << "Let's print some numbers." << endl;
      for (int i = 1; i < 10; ++i) {
        cout << i << "! ";
      }
      i = 10;
      cout << i << "!";
    }