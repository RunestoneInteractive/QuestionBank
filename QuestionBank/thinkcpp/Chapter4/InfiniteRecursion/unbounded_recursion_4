.. mchoice:: unbounded_recursion_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: InfiniteRecursion
   :topics: Chapter4/InfiniteRecursion
   :from_source: T
   :answer_a: The function will print "Not Negative!"
   :answer_b: The function will print "Not Negative!" more than once.  Then it will print "Negative!" and will stop executing.
   :answer_c: The function will print "Negative!"
   :answer_d: The function will never stop executing, there will be infinite recursion.
   :correct: d
   :feedback_a: The function will print "Not Negative!" but it won't stop there!
   :feedback_b: The function will print "Not Negative!" more than once.  But will it print "Negative"?
   :feedback_c: We start with a positive number, so the function simply won't print "Not Negative!"
   :feedback_d: Our input is incremented with every recursive call, so if we start with a positive number, we will never reach the base case.
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   The isNegative function has been **edited** as shown below.  What will
   happen now when we run the code?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       void isNegative(int n) {
         if (n >= 0) {
           cout << "Not Negative!";
           nLines(n + 1);
         }
         cout << "Negative!";
       }
   
       int main() {
         isNegative(10);
       }