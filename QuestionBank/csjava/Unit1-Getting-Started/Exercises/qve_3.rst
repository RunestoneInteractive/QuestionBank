.. mchoice:: qve_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :practice: T
   :answer_a: 0.3333333333333333
   :answer_b: 0
   :answer_c: It will give a run-time error
   :answer_d: 0.3
   :answer_e: It will give a compile-time error
   :correct: b
   :feedback_a: This would be correct if it was 1.0 / 3 or 1 / 3.0.
   :feedback_b: When two integers are divided the results will also be integer and the fractional part is thrown away.
   :feedback_c: You would get a run-time error if it was 1 / 0, because you can not divide by zero.
   :feedback_d: Try it. Is this what you get?
   :feedback_e: Integer division is allowed in Java.  It gives an integer result.

   What does the following code print?

   .. code-block:: java

     System.out.println(1 / 3);