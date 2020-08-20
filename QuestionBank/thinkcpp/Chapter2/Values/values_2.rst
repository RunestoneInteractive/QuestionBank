.. mchoice:: values_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Values
   :topics: Chapter2/Values
   :from_source: F
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :correct: b
   :feedback_a: There is an "endl" statement, implying that a new line is created.
   :feedback_b: "endl" creates one new line. The first line will say 7, while the second will print 777.
   :feedback_c: In C++, you must make sure to say "endl" every time you'd like to create a new line.
   :feedback_d: In C++, you must make sure to say "endl" every time you'd like to create a new line.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   On how many separate lines will the 7's be printed?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main () {
         cout << 7 << endl;
         cout << 7;
         cout << 7;
         cout << 7;
       }