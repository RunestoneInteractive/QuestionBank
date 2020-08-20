.. mchoice:: chained_conditionals_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: ChainedConditionals
   :topics: Chapter4/ChainedConditionals
   :from_source: T
   :answer_a: Three!
   :answer_b: One!
   :answer_c: One! Two!
   :answer_d: One! Two! Three!
   :correct: d
   :feedback_a: Make note of the use of "if" instead of "else if" or "else".
   :feedback_b: Make note of the use of "if" instead of "else if" or "else".
   :feedback_c: Make note of the use of "if" instead of "else if" or "else".
   :feedback_d: When we have "if" statments, but no "else if" or "else", every condition will be checked.
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.5

   What will print after the following code is executed?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main () {
         int x = 10;
         if (x > 8) {
           cout << "One! ";
         }
         if (x > 6) {
           cout << "Two! ";
         }
         if (x > 3) {
           cout << "Three!" << endl;
         }
         return 0;
       }