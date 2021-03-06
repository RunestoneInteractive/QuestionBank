.. mchoice:: qve_new6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: a random number from 0 to 4
   :answer_b: a random number from 1 to 5
   :answer_c: a random number from 5 to 9
   :answer_d: a random number from 5 to 10
   :correct: c
   :feedback_a: This would be true if it was (int) (Math.random * 5)
   :feedback_b: This would be true if it was ((int) (Math.random * 5)) + 1
   :feedback_c: Math.random returns a value from 0 to not quite 1.  When you multiply it by 5 you get a value from 0 to not quite 5.  When you cast to int you get a value from 0 to 4.  Adding 5 gives a value from 5 to 9.
   :feedback_d: This would be true if Math.random returned a value between 0 and 1, but it won't ever return 1.  The cast to int results in a number from 0 to 4.  Adding 5 gives a value from 5 to 9.
   :pct_on_first: 0.3609756098
   :total_students_attempting: 3690
   :num_students_correct: 3668.0
   :mean_clicks_to_correct: 1.9340239913

   Given the following code segment, what is the value of ``num`` when it finishes executing? Math.random() returns a random decimal number between 0 and up to 1, for example 0.4.
   
    .. code-block:: java
   
      double value = Math.random();
      int num = (int) (value * 5) + 5;