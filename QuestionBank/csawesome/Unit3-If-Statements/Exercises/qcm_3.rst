.. mchoice:: qcm_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: Exercises
   :topics: Unit3-If-Statements/Exercises
   :from_source: T
   :practice: T
   :answer_a: x = 0;
   :answer_b: if (x > 0) x = 0;
   :answer_c: if (x < 0) x = 0;
   :answer_d: if (x > 0) x = -x; else x = 0;
   :answer_e: if (x < 0) x = 0; else x = -1;
   :correct: a
   :feedback_a: No matter what x is set to originally, the code will reset it to 0.
   :feedback_b: Even if x is < 0, the above code will set it to 0.
   :feedback_c: Even if x is > than 0 originally, it will be set to 0 after the code executes.
   :feedback_d: The first if statement will always cause the second to be executed unless x already equals 0, such that x will never equal -x.
   :feedback_e: The first if statement will always cause the second to be executed unless x already equals 0, such that x will never equal -x.
   :pct_on_first: 0.288231383
   :total_students_attempting: 3008
   :num_students_correct: 2970.0
   :mean_clicks_to_correct: 3.363973064

   Which of the following is equivalent to the code segment below?
   
   .. code-block:: java
   
     if (x > 0)
        x = -x;
     if (x < 0)
        x = 0;