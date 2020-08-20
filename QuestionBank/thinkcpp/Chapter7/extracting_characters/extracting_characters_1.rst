.. mchoice:: extracting_characters_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: extracting_characters
   :topics: Chapter7/extracting_characters
   :from_source: T
   :practice: T
   :answer_a: 1
   :answer_b: 0
   :answer_c: 2
   :correct: b
   :feedback_a: Don't forget that computer scientists do not start counting at 1!
   :feedback_b: Yes, this would access the letter "b".
   :feedback_c: This would access the letter "k".
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   What would replace the "?" in order to access the letter "b" in the string below?
   
   .. code-block:: cpp
      :linenos:
   
      #include <iostream>
      using namespace std;
   
      int main () {
        string bake = "bake a cake!";
        char letter = bake[?];
      }