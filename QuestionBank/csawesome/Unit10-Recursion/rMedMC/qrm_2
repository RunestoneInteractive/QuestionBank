.. mchoice:: qrm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rMedMC
   :topics: Unit10-Recursion/rMedMC
   :from_source: T
   :practice: T
   :answer_a: 243
   :answer_b: 0
   :answer_c: 3
   :answer_d: 81
   :answer_e: 27
   :correct: a
   :feedback_a: For the call <code>mystery(5)</code>, <code>n != 0</code> so the <code>else</code> statement is executed. This results in the next recursive call of <code>mystery(4)</code>. This will continue until the call <code>mystery(0)</code> is executed. At this point, the value 1 will be returned. Then each call of <code>mystery</code> can return with the 3 * the result of the recursive call. So this method will compute 3 to the given power.
   :feedback_b: This can never be 0 because the stopping condition returns 1 when you call <code>mystery(0)</code>
   :feedback_c: This would only be true if you called <code>mystery(1)</code>
   :feedback_d: This would be true if you called <code>mystery(4)</code>
   :feedback_e: This would be true if you called <code>mystery(3)</code>
   :pct_on_first: 0.5755102041
   :total_students_attempting: 490
   :num_students_correct: 485.0
   :mean_clicks_to_correct: 1.8164948454

   Given the following method declaration, what value is returned as the result of the call ``mystery(5)``?
   
   .. code-block:: java
      :linenos:
   
      public static int mystery(int n)
      {
         if (n == 0)
            return 1;
         else
            return 3 * mystery (n - 1);
      }