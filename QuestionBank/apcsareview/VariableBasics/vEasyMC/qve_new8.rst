.. mchoice:: qve_new8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: vEasyMC
   :topics: VariableBasics/vEasyMC
   :from_source: T
   :answer_a: a random number from 0 to 10
   :answer_b: a random number from 0 to 9
   :answer_c: a random number from -5 to 4
   :answer_d: a random number from -5 to 5
   :correct: d
   :feedback_a: This would be true if it was (int) (value * 11)
   :feedback_b: This would be true if it was (int) (value * 10)
   :feedback_c: This would be true if it was (int) (value * 10) - 5
   :feedback_d: Math.random returns a random value from 0 to not quite 1.  After it is multipied by 11 and cast to integer it will be a value from 0 to 10.  Subtracting 5 means it will range from -5 to 5.

   Given the following code segment, what is the value of ``num`` when it finishes executing?

    .. code-block:: java

      double value = Math.random();
      int num = (int) (value * 11) - 5;