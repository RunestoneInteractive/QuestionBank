.. mchoice:: pass_others_reference_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: passing_other_types_by_reference
   :topics: Chapter8/passing_other_types_by_reference
   :from_source: T
   :practice: T
   :answer_a: x, y, z
   :answer_b: x, y, z, q
   :answer_c: a, b
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Pay attention to the placement of the ``&``
   :feedback_c: Pay attention to the placement of the ``&``
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   What of the parameters in the following code block are pass-by-reference?
   
   .. code-block:: cpp
   
      void swap (int& x, int& y) {
        int temp = x;
        x = y;
        y = temp;
      }
   
      void add (int& z, int q) {
        z = z + y;
      }
   
      int multiply (int a, int b) {
        int total = a * b;
        return total;
      }