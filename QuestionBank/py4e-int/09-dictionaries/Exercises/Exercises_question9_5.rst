.. mchoice:: Exercises_question9_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: Exercises
   :topics: 09-dictionaries/Exercises
   :from_source: T
   :practice: T
   :answer_a: fruits.get(apples)
   :answer_b: fruits.get('apples', 0)
   :answer_c: fruits.get('apple')
   :answer_d: fruits.get(apples, 0)
   :correct: b
   :feedback_a: Try again!
   :feedback_b: Correct! This correctly grabs the key as a string, and also includes a default value in case the key is not present in the dictionary.
   :feedback_c: Try again!
   :feedback_d: Try again!

   Which line of code correctly grabs the value of the key 'apples'?

   .. code-block:: python

      fruits = {'bananas': 7, 'apples': 4, 'grapes': 19, 'pears': 4}