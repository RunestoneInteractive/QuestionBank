.. mchoice:: switch_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: switch_statement
   :topics: Chapter13/switch_statement
   :from_source: T
   :answer_a: 4
   :answer_b: 49
   :answer_c: 49Invalid num! Please try again.
   :answer_d: Invalid num! Please try again.
   :answer_e: Code will not run.
   :correct: c
   :feedback_a: Where do we / don't we encounter a break statement?
   :feedback_b: Where do we / don't we encounter a break statement?
   :feedback_c: Notice that 2 is not an invalid number, but since we are missing break statements, multiple branches execute.
   :feedback_d: Is 2 one of the invalid numbers?
   :feedback_e: There is no reason why the code wouldn't run.

   And finally, what about **this time**?

   .. code-block:: cpp

      int main() {
        int num = 2;

        switch (num) {
        case 1:
          cout << 1;
          break;
        case 2:
          cout << 4;
        case 3:
          cout << 9;
        default:
          cout << "Invalid num! Please try again.";
        }
      }