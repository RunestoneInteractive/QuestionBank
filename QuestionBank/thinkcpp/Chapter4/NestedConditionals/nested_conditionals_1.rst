.. mchoice:: nested_conditionals_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: NestedConditionals
   :topics: Chapter4/NestedConditionals
   :from_source: T
   :answer_a: Hey!
   :answer_b: Hi!
   :answer_c: Hello!
   :answer_d: Nothing will print.
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Remember that the program would only enter the "else" if x was not equal to 0.
   :feedback_c: Remember that the program would only enter the "else" if x was not equal to 0.
   :feedback_d: Only one of the condtionals will execute, but something will print, regardless of which one it is.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   What will print?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main () {
         int x = 0;
         if (x == 0) {
           cout << "Hey!" << endl;
         }
         else {
           if (x > 0) {
             cout << "Hi!" << endl;
           }
           else {
             cout << "Hello!" << endl;
           }
         }
         return 0;
       }