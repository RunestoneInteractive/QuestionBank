.. mchoice:: chained_conditionals_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: ChainedConditionals
   :topics: Chapter4/ChainedConditionals
   :from_source: T
   :answer_a: Two!
   :answer_b: Two! Three!
   :answer_c: One! Two!
   :answer_d: One! Two! Three!
   :correct: a
   :feedback_a: Only one action will is completed in a chain of "ifs", "else ifs", and "ifs";
   :feedback_b: Remember that only one action will be completed in a chain of "ifs", "else ifs", and "ifs".
   :feedback_c: The first condition will not be satisfied.  Also, a chain of "ifs", "else ifs", and "elses" will result in only one action being completed.
   :feedback_d: hge first condition will not be satisfied.  Also, a chain of "ifs", "else ifs", and "elses" will result in only one action being completed.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   What will print after the following code is executed?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main () {
         int x = 7;
         if (x > 8) {
           cout << "One! " ;
         }
         else if (x > 6) {
           cout << "Two! ";
         }
         else {
           cout << "Three!" << endl;
         }
         return 0;
       }