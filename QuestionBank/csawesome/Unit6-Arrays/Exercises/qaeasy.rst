.. mchoice:: qaeasy
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: Exercises
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: {1, 3, -5, -2}
   :answer_b: {3, 9, -15, -6}
   :answer_c: {2, 6, -10, -4}
   :answer_d: The code will never stop executing due to an infinite loop
   :correct: d
   :feedback_a: Does the value of i ever change inside the loop?
   :feedback_b: Does the value of i ever change inside the loop?
   :feedback_c: Does the value of i ever change inside the loop?
   :feedback_d: The value of i is initialized to 0 and then never changes inside the body of the loop, so this loop will never stop.  It is an infinite loop.
   :pct_on_first: 0.3463869464
   :total_students_attempting: 2145
   :num_students_correct: 2102.0
   :mean_clicks_to_correct: 2.1446241675

   What are the values in a after mult(2) executes?
   
   .. code-block:: java
   
     private int[ ] a = {1, 3, -5, -2};
   
     public void mult(int amt)
     {
        int i = 0;
        while (i < a.length)
        {
           a[i] = a[i] * amt;
        } // end while
     } // end method