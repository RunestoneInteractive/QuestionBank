.. mchoice:: Exercises_question11_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: Exercises
   :topics: 11-regex/Exercises
   :from_source: T
   :answer_a: It will cost you $1.00
   :answer_b: From: stephen.marquard@uct.ac.za $
   :answer_c: $2.50 is your change
   :correct: a, c
   :feedback_a: Correct! There is a dollar sign followed by one or more characters.
   :feedback_b: Try again!
   :feedback_c: Correct. The dollar sign in this line is followed by more than one character.

   Which of these lines will be matched when the following code is run?

   .. code-block:: python

      import re
      hand = open('mbox-short.txt')
      for line in hand:
          line = line.rstrip()
          if re.search('$.+', line):
              print(line)