.. mchoice:: question9_1_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: py4e-int
  :chapter: 09-dictionaries
  :subchapter: 09-dictionaries1
  :topics: 09-dictionaries/09-dictionaries1
  :from_source: T
  :practice: T
  :answer_a: True
  :answer_b: False
  :correct: b
  :feedback_a: Try again!
  :feedback_b: Correct! 'Water' is a value in the dictionary, therefore the in operator will not be able to determine if this is in the dictionary.

  What is printed after the following code is run?

  .. code-block:: python

     pokemon_name_n_type = {'Squirtle': 'Water', 'Charmander': 'Fire', 'Bulbasaur' : 'Grass'}
     print('Water' in pokemon_name_n_type)