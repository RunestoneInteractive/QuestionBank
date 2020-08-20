.. mchoice:: arrayEx1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: arrayExam
   :topics: Unit6-Arrays/arrayExam
   :from_source: T
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: c
   :feedback_a: While i is set to 0 initially it does change.
   :feedback_b: This would be true if i was incremented after the sum was changed instead of before.
   :feedback_c: This will loop twice and increment i each time so at the end i is 2.
   :feedback_d: This would be true if it was asking for the value of limit.
   :pct_on_first: 0.5598130841
   :total_students_attempting: 1070
   :num_students_correct: 727.0
   :mean_clicks_to_correct: 1.2324621733

   What is the value of ``i`` after the following code has executed?
   
   
   .. code-block:: java
   
     int[] x = {2, 1, 4, 5, 7};
     int limit = 3;
     int i = 0;
     int sum = 0;
     while ((sum < limit) && (i < x.length))
     {
        i++;
        sum = sum + x[i];
     }