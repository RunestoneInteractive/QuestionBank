.. mchoice:: Exercises_question9_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: Exercises
   :topics: 09-dictionaries/Exercises
   :from_source: T
   :practice: T
   :answer_a: jan, chuck, annie
   :answer_b: chuck, annie, jan
   :answer_c: annie, chuck, jan
   :correct: a, b, c
   :feedback_a: Correct! When written like this, they keys will not come out in any particular order. If you want them ordered, you have to use the sort function.
   :feedback_b: Correct! When written like this, they keys will not come out in any particular order. If you want them ordered, you have to use the sort function.
   :feedback_c: Correct! When written like this, they keys will not come out in any particular order. If you want them ordered, you have to use the sort function.

   What order do the keys print in after the following code is run? (Select all that apply)

   .. code-block:: python

      counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
      for key in counts:
          print(key, counts[key])