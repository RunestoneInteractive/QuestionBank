.. mchoice:: stack_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: StackDiagrams
   :topics: Chapter4/StackDiagrams
   :from_source: T
   :answer_a: 3
   :answer_b: 4
   :answer_c: 5
   :answer_d: infinite
   :correct: d
   :feedback_a: If nLines could reach its base case, it cannot be done in 3 function calls.
   :feedback_b: If nLines could reach its base case, it cannot be done in 4 function calls.
   :feedback_c: If nLines could reach its base case, it could be done in 5 function calls, but does it ever reach the base case?
   :feedback_d: The nLines function never reaches its base case, so the stack diagram would be infinitely long.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Refer to the ``nLines`` function below.  It is the same as the ``nLines``
   function defined on the previous page.  How many instances of ``nLines``
   would there be in the stack diagram if we begin with n = 4?
   
   ::
   
       void nLines(int n) {
         if (n > 0) {
           cout << endl;
           nLines(n + 1);
         }
       }