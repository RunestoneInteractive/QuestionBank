.. mchoice:: retention_8_F16_q26
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: Exercises
   :topics: CSPIntroDecisions/Exercises
   :from_source: F
   :answer_a: [106]
   :answer_b: [206, 110]
   :answer_c: [106, 206]
   :answer_d: There is an error
   :answer_e: None
   :feedback_a: Incorrect!
   :feedback_b: Incorrect!
   :feedback_c: Correct!
   :feedback_d: Incorrect!
   :feedback_e: Incorrect!
   :correct: c
   :practice: T

   What will print when the following code runs? If there is an error, say so.

   .. sourcecode:: python

      lstA = [106]
      lstB = lstA
      lstA.append(206)
      lstA = lstA[1:]
      lstA.append(506)
      print(lstB)