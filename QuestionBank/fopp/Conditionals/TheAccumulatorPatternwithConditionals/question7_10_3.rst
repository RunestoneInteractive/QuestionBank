.. mchoice:: question7_10_3
   :author: Brad Miller
   :difficulty: 3.5245901639
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: TheAccumulatorPatternwithConditionals
   :topics: Conditionals/TheAccumulatorPatternwithConditionals
   :from_source: F
   :answer_a: I
   :answer_b: II
   :answer_c: III
   :answer_d: IV
   :correct: c
   :feedback_a: c will be bound to a key, which is a string; you can't compare that to a number.
   :feedback_b: That will treate the current value of a as a key in the dictionary and update that key's value. You want to update a instead.
   :feedback_c: When the value associated with the current key c is bigger than the max so far, replace the max so far with that value.
   :feedback_d: That will set a to be the current key, a string like 'a', not a value like 194.
   :practice: T
   :pct_on_first: 0.368852459
   :total_students_attempting: 122
   :num_students_correct: 122.0
   :mean_clicks_to_correct: 2.0409836066

   Which is the right code block to use in place of line 5 if we want to print out the maximum value?
   
   .. code-block:: python
   
      d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
   
      a = 0
      for c in d:
        # <what code goes here? See below options>
   
      print("max value is " + a)
   
   
   .. code-block:: python
   
      # I.
      if c > a:
         a = c
   
      # II.
      if d[c] > a:
         d[a] = c
   
      # III.
      if d[c] > a:
         a = d[c]
   
      # IV.
      if d[c] > a:
         a = c