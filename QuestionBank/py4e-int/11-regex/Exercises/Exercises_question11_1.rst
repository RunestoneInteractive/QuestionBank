.. mchoice:: Exercises_question11_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: Exercises
   :topics: 11-regex/Exercises
   :from_source: T
   :practice: T
   :answer_a: Any line containing the word 'From'
   :answer_b: Any line that starts with 'From'
   :answer_c: Any line that starts with 'From:'
   :correct: c
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Correct! The regex equation will match with any line beginning with 'From:'.

   What will the following code print?

   .. code-block:: python

      import re
      hand = open('mbox-short.txt')
      for line in hand:
          line = line.rstrip()
          if re.search('^From:', line):
              print(line)