.. mchoice:: qve_new7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :practice: T
   :answer_a: It will print 0
   :answer_b: It will give a run-time error
   :answer_c: It will give a compile-time error (won't compile)
   :answer_d: It will print 5
   :correct: b
   :feedback_a: This would be true if it was System.out.println(0 / 5)
   :feedback_b: You can't divide by 0 so this cause a run-time error.
   :feedback_c: You might think that this would be caught at compile time, but it isn't.
   :feedback_d: This would be true if it was System.out.println(5 / 1)

   What does the following code do when it is executed?

    .. code-block:: java

      System.out.println(5 / 0);