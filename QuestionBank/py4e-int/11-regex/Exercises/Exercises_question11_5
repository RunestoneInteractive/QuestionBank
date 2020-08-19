.. mchoice:: Exercises_question11_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: Exercises
   :topics: 11-regex/Exercises
   :from_source: T
   :practice: T
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Try again!
   :feedback_b: Correct! The '+' character in regex is greedy, therefore it will match with the entire string and not just one email.

   True or false, the following code will match only the first email(up to the @ sign) in the string?

   .. code-block:: python

      import re
      stri = 'From: stephen.a.smith@espn.com, drake@hotmail.com, frenchMontana@gmail.com'
      stri = stri.rstrip()
      print(re.findall('From:.+@', stri))