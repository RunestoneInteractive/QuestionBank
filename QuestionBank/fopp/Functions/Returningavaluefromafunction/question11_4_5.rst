.. mchoice:: question11_4_5
   :author: bmiller
   :difficulty: 2.2094915254
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Returningavaluefromafunction
   :topics: Functions/Returningavaluefromafunction
   :from_source: T
   :answer_a: 1
   :answer_b: Yes
   :answer_c: First one was longer
   :answer_d: Second one was at least as long
   :answer_e: Error
   :correct: c
   :feedback_a: cyu2 returns the value 1, but that's not what prints.
   :feedback_b: "Yes" is longer, but that's not what prints.
   :feedback_c: cyu2 returns the value 1, which is assigned to z.
   :feedback_d: cyu2 returns the value 1, which is assigned to z.
   :feedback_e: what do you think will cause an error.
   :practice: T
   :pct_on_first: 0.6976271186
   :total_students_attempting: 1475
   :num_students_correct: 1467.0
   :mean_clicks_to_correct: 1.5167007498

   What will the following code output?
   
   .. code-block:: python
   
       def cyu2(s1, s2):
           x = len(s1)
           y = len(s2)
           return x-y
   
       z = cyu2("Yes", "no")
       if z > 0:
           print("First one was longer")
       else:
           print("Second one was at least as long")