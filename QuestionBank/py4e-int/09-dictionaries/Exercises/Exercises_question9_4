.. mchoice:: Exercises_question9_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: Exercises
   :topics: 09-dictionaries/Exercises
   :from_source: T
   :practice: T
   :answer_a: 5
   :answer_b: 10
   :answer_c: 9
   :correct: c
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Correct! There are 9 letters in phrase that appear more than two times.

   What is the value of counter after the code is run to completion?

   .. code-block:: python

      phrase = "Cheese in Philadelphia is extraordinary according to Erik"

      counter = 0
      letters = {}
      for word in phrase.split():
          for letter in word:
              letter = letter.lower()
              if letter not in letters.keys():
                  letters[letter] = 0
              letters[letter] += 1
      for key in letters.keys():
          if letters[key] > 2:
              counter += 1