.. mchoice:: return_vals_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: returnvalues
   :topics: Chapter5/returnvalues
   :from_source: T
   :answer_a: 4
   :answer_b: 2
   :answer_c: 16
   :answer_d: The function does not return.
   :correct: b
   :feedback_a: The function returns y before reaching the line where y is doubled.
   :feedback_b: Because the return statement in the timesTwo function returns prior to the modification of y, 2 is returned and then printed.
   :feedback_c: The function returns y before reaching the line where y is doubled.
   :feedback_d: The function has an integer return type, so it WILL return an int.
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   What will print?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int timesTwo(int x) {
         int y = x;
         return y;
         y = y * 2;
       }
   
       int main () {
         int i = 2;
         cout << timesTwo(i);
         return 0;
       }