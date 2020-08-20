.. mchoice:: accessing_instance_variables_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: accessing_instance_variables
   :topics: Chapter8/accessing_instance_variables
   :from_source: T
   :practice: T
   :answer_a: int y = circle.x();
   :answer_b: int circle = x.y;
   :answer_c: int y = circle.x;
   :answer_d: int x = circle.y;
   :correct: d
   :feedback_a: No parentheses are needed.
   :feedback_b: You should be assigning to the local variable x.
   :feedback_c: You should be assigning to the local variable x.
   :feedback_d: This is the correct way to assign the value of y to x.
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   You want to go to the object named ``circle`` and get the value of ``y``, then assign it to the local variable ``x``. How would you do that?