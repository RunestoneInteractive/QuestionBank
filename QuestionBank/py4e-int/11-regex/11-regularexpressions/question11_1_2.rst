.. mchoice:: question11_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-regularexpressions
   :topics: 11-regex/11-regularexpressions
   :from_source: T
   :practice: T
   :answer_a: Any line that contains a 'B'
   :answer_b: Any line containing 'b'
   :answer_c: Lines starting with the letter 'b'
   :correct: b
   :feedback_a: Try again!
   :feedback_b: Correct! Since there is no ^ before the 'b', we are only looking at lines that contain the letter 'b'.
   :feedback_c: Try again!

   Which lines will the following code print?

   .. code-block:: python

      import re
      hand = open('mbox-short.txt')
      for line in hand:
          line = line.rstrip()
          if re.search('b', line):
              print(line)