.. mchoice:: qse_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :practice: T
   :answer_a: xyz
   :answer_b: xyxyz
   :answer_c: xy xy z
   :answer_d: xy z
   :answer_e: z
   :correct: b
   :feedback_a: s1 will equal "xy" plus another "xy" then z at the end.
   :feedback_b: s1 contains the original value, plus itself, plus "z"
   :feedback_c: No spaces are added during concatenation.
   :feedback_d: No spaces are added during concatenation, and an additional "xy" should be included at the beginning.
   :feedback_e: s1 was set to "xy" initially, so the final answer will be "xyxyz"
   :pct_on_first: 0.81002331
   :total_students_attempting: 5148
   :num_students_correct: 5118.0
   :mean_clicks_to_correct: 1.3161391168

   Given the following code segment, what is in the string referenced by s1?
   
   .. code-block:: java
   
     String s1 = "xy";
     String s2 = s1;
     s1 = s1 + s2 + "z";