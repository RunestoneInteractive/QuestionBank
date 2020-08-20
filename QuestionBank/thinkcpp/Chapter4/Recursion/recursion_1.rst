.. mchoice:: recursion_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: Recursion
   :topics: Chapter4/Recursion
   :from_source: T
   :answer_a: !
   :answer_b: !!
   :answer_c: !!!
   :answer_d: !!!!
   :correct: c
   :feedback_a: The function keeps executing while n is greater than 0.
   :feedback_b: The function keeps executing while n is greater than 0.
   :feedback_c: Correct! First, the program enters the if statement within exclamationPoint because n is greater than 0. Then the function prints a "!" and calls itself again, but with n-1, which is 2. This repeats until n is 0, which is when the program exits the function.
   :feedback_d: The function keeps executing while n is greater than 0. Therefore, when n is 0, it will not print a "!"
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.3333333333

   What will print?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       void exclamationPoint(int n) {
         if (n > 0) {
           cout << "!";
           exclamationPoint (n-1);
         }
       }
   
       int main () {
         exclamationPoint(3);
       }