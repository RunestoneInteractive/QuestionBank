.. mchoice:: question9_2_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionarycounters
   :topics: 09-dictionaries/09-dictionarycounters
   :from_source: T
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: None
   :correct: a
   :feedback_a: Correct! Since there isn't a "d" in word, the code returns the default value.
   :feedback_b: Try again!
   :feedback_c: Try again!

   What does the following code print?

   .. code-block:: python

      word = "incomprehensible"
      d = dict()
      for char in word:
          if char not in d:
              d[char] = 1
          else:
              d[char] = d[char] + 1
      print(d.get('d', 0))