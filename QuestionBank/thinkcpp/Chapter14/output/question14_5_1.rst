.. mchoice:: question14_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: output
   :topics: Chapter14/output
   :from_source: T
   :practice: T
   :answer_a: 5 e^ 0.927295i
   :answer_b: 3 + 4i
   :answer_c: 2 + 3i
   :answer_d: 5 e^ 1
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Incorrect! Try using the active code above.
   :feedback_c: Incorrect! Try using the active code above.
   :feedback_d: Incorrect! Try using the active code above.

   What is the correct output of the code below?

   .. code-block:: cpp

      int main() {
        Complex c1 (3.0, 4.0);
        // c1.printCartesian();
        c1.printPolar();
      }