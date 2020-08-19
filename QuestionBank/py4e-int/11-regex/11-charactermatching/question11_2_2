.. mchoice:: question11_2_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-charactermatching
   :topics: 11-regex/11-charactermatching
   :from_source: T
   :practice: T
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