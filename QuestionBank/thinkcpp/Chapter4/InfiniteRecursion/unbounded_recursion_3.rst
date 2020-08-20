.. mchoice:: unbounded_recursion_3
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
   :correct: b
   :feedback_a: The function will print "Not Negative!", but it won't stop there!
   :feedback_b: The function will print "Not Negative!" until it reaches a negative number.
   :feedback_c: The function will eventually print "Not Negative!", but that's not all!
   :feedback_d: Since we decrement each time, the base case will be reached.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Suppose we have already defined isNegative (see previous question).
   What will happen if we run the code with this input?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       int main() {
         isNegative(10);
       }