.. mchoice:: own_version_find_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: own_version_find
   :topics: Chapter7/own_version_find
   :from_source: T
   :practice: T
   :answer_a: 13, -1, 8
   :answer_b: 13, 0, 7
   :answer_c: 13, -1, 0
   :answer_d: 14, -1, 9
   :correct: a
   :feedback_a: Notice how the built-in find function works differently from ours.
   :feedback_b: Remember that when a character isn't found, the function returns -1.
   :feedback_c: Keep in mind that the find function is case sensitive, so "A" is different from "a".
   :feedback_d: Remember that indexing begins at 0 for C++.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 4.0

   What is the correct output of the code below?
   
   .. code-block:: cpp
   
      int main() {
        string quote = "The way to get started is to quit talking and begin doing.";
        cout << find(quote, 't', 11) << ", " << find(quote, 't', 42) << ", " << quote.find('t');
      }