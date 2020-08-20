.. mchoice:: question10_4_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-dictionariesandtuples
   :topics: 10-tuples/10-dictionariesandtuples
   :from_source: T
   :practice: T
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Try again!
   :feedback_b: Correct! Parentheses are required when calling the .items() method.

   True or false? The following code will correctly output the items of the dictionary t.

   .. code-block:: python

      name_dictionary = {'Bob': 5, 'Melissa': 3, 'John': 7, 'Kim': 5}
      t = list(name_dictionary.items)
      print(t)