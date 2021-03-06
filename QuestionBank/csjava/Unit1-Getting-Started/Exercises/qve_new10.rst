.. mchoice:: qve_new10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :practice: T
   :answer_a: x = 3, y = 3, z = 9
   :answer_b: x = 4, y = 3, z = 9
   :answer_c: x = 0, y = 3, z = 0
   :answer_d: x = 4, y = 4, z = 9
   :correct: b
   :feedback_a: This would be true if the x++ wasn't there.
   :feedback_b: First x is set to 3, then y is also set to 3, and next z is set to 3 * 3 = 9.  Finally x is incremented to 4.
   :feedback_c: You might think that y = x means that y takes x's value, but y is set to a copy of x's value.
   :feedback_d: You might think that y = x means that if x is incremented that y will also be incremented, but y = x only sets y to a copy of x's value and doesn't keep them in sync.

   What are the values of x, y, and z after the following code executes?

    .. code-block:: java

      int x = 3;
      int y = x;
      int z = x * y;
      x++;