.. mchoice:: question10_7_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-usingtuplesaskeys
   :topics: 10-tuples/10-usingtuplesaskeys
   :from_source: T
   :practice: T
   :answer_a: my_dict['Go']
   :answer_b: my_dict[Blue']
   :answer_c: my_dict['Go', 'Blue']
   :answer_d: my_dict[('Go', 'Blue')]
   :correct: c, d
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Correct! The parentheses of the tuple are not required in order to properly call its value.
   :feedback_d: Correct! This is how to grab the value associated with the tuple.s

   Which of the following lines of code correctly prints the value associated with ('Go', 'Blue')? Select all that apply.

   .. code-block:: python

      my_dict = {}
      my_dict[('Go', 'Blue')] = True