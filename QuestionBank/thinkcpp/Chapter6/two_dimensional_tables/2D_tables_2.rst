.. mchoice:: 2D_tables_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: two_dimensional_tables
   :topics: Chapter6/two_dimensional_tables
   :from_source: T
   :answer_a: Change the first output statement to say cout << 3*x << endl;
   :answer_b: Change the first output statement to say cout << 3*x << \n;
   :answer_c: Change the second output statement to say cout << endl << endl;
   :answer_d: This code already prints each multiple on its own line.
   :correct: a
   :feedback_a: The addition of the endl will print the multiples of three on separate lines.
   :feedback_b: A newline character must be used in conjunction with a string. In this case, we are outputting an integer. To use a newline character in this scenario you must use quotes around it. (ex. "\n")
   :feedback_c: This would simply print out two new lines after all of the multiples have already printed on one line.
   :feedback_d: This code prints all multiples out on one line.

   Currently, the code below prints all of the multiples of three on one line. How can you change the output so that each multiple prints on its own line?

   .. code-block:: cpp

    #include <iostream>
    using namespace std;

    int main() {
      int x = 1;
      while (x <= 6) {
        cout << 3*x << "  ";
        x = x + 1;
      }
      cout << endl;
      return 0;
    }