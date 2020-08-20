.. mchoice:: looping_counting_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: looping_and_counting
   :topics: Chapter7/looping_and_counting
   :from_source: T
   :practice: T
   :answer_a: 5 4 3 2 1
   :answer_b: -5 -4 -3 -2 -1
   :answer_c: -4 -3 -2 -1 0
   :correct: c
   :feedback_a: Notice that x is negative.
   :feedback_b: Notice that the value of x is incremented before it is printed.
   :feedback_c: The value of x is incremented before it is printed so the first value printed is -4.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   What does the following code print?
   
   .. code-block:: cpp
      :linenos:
   
      int x = -5;
      while (x < 0) {
        x = x + 1;
        cout << x << " ";
      }