.. mchoice:: JP_qcbdm3_1
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: F
   :answer_a: (x < 2) || (y > 4)
   :answer_b: (x < 2) && (y > 4)
   :answer_c: (x <= 2) || (y >= 4)
   :answer_d: (x <= 2) && (y >= 4)
   :correct: c
   :feedback_a: The negation of x > 2 is x <= 2
   :feedback_b: Don't forget that the and is changed to an or
   :feedback_c: The x > 2 becomes x <= 2, the y < 4 becomes y >= 4 and the and changes to or
   :feedback_d: Don't forget that the and is changed to an or
   :pct_on_first: 0.4857142857
   :total_students_attempting: 35
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.9

   Which of the following is the same as the code below?
   
   .. code-block:: java
   
     !(x > 2 && y < 4)