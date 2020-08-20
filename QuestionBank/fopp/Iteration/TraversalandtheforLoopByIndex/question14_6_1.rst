.. mchoice:: question14_6_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: TraversalandtheforLoopByIndex
   :topics: Iteration/TraversalandtheforLoopByIndex
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :answer_e: 6
   :correct: d
   :feedback_a: idx % 2 is 0 whenever idx is even
   :feedback_b: idx % 2 is 0 whenever idx is even
   :feedback_c: idx % 2 is 0 whenever idx is even
   :feedback_d: idx % 2 is 0 whenever idx is even
   :feedback_e: idx % 2 is 0 whenever idx is even
   :practice: T
   :pct_on_first: 0.3401015228
   :total_students_attempting: 1773
   :num_students_correct: 1752.0
   :mean_clicks_to_correct: 2.7471461187

   How many times is the letter p printed by the following statements?
   
   .. code-block:: python
   
      s = "python"
      for idx in range(len(s)):
         print(s[idx % 2])