.. parsonsprob:: mucp_5_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: mixed_up_code
   :topics: Chapter5/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 5.0

   Most assignments and tests are graded as a percentage, but final
   grades are letters. Let's write the code for the ``percentToLetter`` function.
   ``percentToLetter`` takes a ``double percentage`` and returns the corresponding
   letter grade. A 90 and above is an 'A', an 80 and above is a 'B', a 70 and above
   is a 'C', a 60 and above is a 'D', and anything under a 60 is an 'F'.
   Put the necessary blocks of code in the correct order.
   -----
   char percentToLetter (double percentage) {
   =====
   void percentToLetter (double percentage) {  #distractor
   =====
   char percentToLetter (int percentage) {  #distractor
   =====
   char percentToLetter (percentage) {  #distractor
   =====
      if (percentage >= 90) {
   =====
         return 'A';
      }
   =====
         return A;  #paired
      }
   =====
      else if (percentage >= 80) {
   =====
         return 'B';
      }
   =====
         return 'B'  #paired
      }
   =====
      else if (percentage >= 70) {
   =====
      else if (percentage > 70) {  #paired
   =====
         return 'C';
      }
   =====
      else if (percentage >= 60) {
   =====
      else if (percentage = 60) {  #paired
   =====
         return 'D';
      }
   =====
      else {
   =====
         return 'F';
      }
   =====
   }