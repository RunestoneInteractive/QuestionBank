.. mchoice:: assignment_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Assignment
   :topics: Chapter2/Assignment
   :from_source: T
   :answer_a: Change the type of variable q from int to char.
   :answer_b: Change the type of both variables (p and q) from int to char.
   :answer_c: Change the type of variable p from int to char.
   :answer_d: Nothing needs to change! The code will work just fine!
   :correct: b
   :feedback_a: Yes, but take a look at variable p.
   :feedback_b: Both variables are a character surrounded by single quotes, so they should be type char.
   :feedback_c: Yes, but take a look at variable q.
   :feedback_d: No! There will be a compile error.
   :pct_on_first: 0.4
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.6

   What must be changed in order for this code block to work?
   
   ::
   
       #include <iostream>
       using namespace std;
       // main: generate some simple output
   
       int main () {
         int p;
         int q;
         p = 'h';
         q = '9';
       }