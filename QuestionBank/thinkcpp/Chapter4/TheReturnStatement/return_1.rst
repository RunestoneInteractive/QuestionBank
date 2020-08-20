.. mchoice:: return_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: TheReturnStatement
   :topics: Chapter4/TheReturnStatement
   :from_source: T
   :answer_a: One! Two! Three!
   :answer_b: Two! Three!
   :answer_c: Three!
   :answer_d: Two!
   :answer_e: One!
   :correct: d
   :feedback_a: Try again! Remember the function of return 0.
   :feedback_b: Try again! Remember the function of return 0.
   :feedback_c: Try again! Remember the function of return 0.
   :feedback_d: 8 is not greater than 8, so the first condition will not be met.
   :feedback_e: Take a look at the first conditional statement more closely.
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.0

   What will print?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main () {
         int x = 8;
         if (x > 8) {
           cout << "One! ";
           return 0;
         }
         if (x > 6) {
           cout << "Two! ";
           return 0;
         }
         if (x > 3) {
           cout << "Three!" << endl;
           return 0;
         }
         return 0;
       }