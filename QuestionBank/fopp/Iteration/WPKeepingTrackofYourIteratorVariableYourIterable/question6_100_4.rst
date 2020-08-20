.. mchoice:: question6_100_4
   :author: bmiller
   :difficulty: 3.1809408926
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: WPKeepingTrackofYourIteratorVariableYourIterable
   :topics: Iteration/WPKeepingTrackofYourIteratorVariableYourIterable
   :from_source: T
   :answer_a: string
   :answer_b: list
   :answer_c: tuple
   :answer_d: iterable
   :answer_e: error, unable to iterate over the object.
   :feedback_a: Incorrect, the iterable is not a string.
   :feedback_b: Incorrect, there is no list in the code.
   :feedback_c: Yes, the iterable in this situation is a tuple.
   :feedback_d: Incorrect, that is not the best answer for this problem.
   :feedback_e: Incorrect, Python can iterate over this type.
   :correct: c
   :practice: T
   :pct_on_first: 0.4547647768
   :total_students_attempting: 1658
   :num_students_correct: 1653.0
   :mean_clicks_to_correct: 2.1488203267

   What is the type of your iterable?
   
   .. sourcecode:: python
   
       t = ("couch", "chair", "washer", "dryer", "table")
       for z in t:
           print(z)