.. mchoice:: Exercises_question9_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: Exercises
   :topics: 09-dictionaries/Exercises
   :from_source: T
   :practice: T
   :answer_a: ['Emily', 'John', 'Erik']
   :answer_b: ['Janice', 'Emily', 'John']
   :answer_c: ['Janice', 'John', 'Erik']
   :correct: a
   :feedback_a: Correct! Erik is initialized to 22, and Emily is updated to 13, therefore these two entries are added to the list found in the prior question.
   :feedback_b: Try again!
   :feedback_c: Try again!

   What does the following code print now that it has been updated?

   .. code-block:: python

      names = {'Janice': 5, 'Emily': 3, 'John': 7, 'Eleanor': 2}
      list_o_names = []

      names['Emily'] += 10
      names['Erik'] = 22

      for name in names:
          if names[name] > 5:
              list_o_names.append(name)
      print(list_o_names)