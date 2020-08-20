.. mchoice:: question6_100_8
   :author: bmiller
   :difficulty: 1.9381188119
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: WPKeepingTrackofYourIteratorVariableYourIterable
   :topics: Iteration/WPKeepingTrackofYourIteratorVariableYourIterable
   :from_source: T
   :answer_a: string
   :answer_b: list
   :answer_c: tuple
   :answer_d: integer
   :answer_e: error, unable to iterate and initialize the iterator variable
   :feedback_a: Yes, the second item in t is a string.
   :feedback_b: Incorrect, that is the type of the iterable, not the iterator variable.
   :feedback_c: Incorrect, there is no tuple in the code.
   :feedback_d: Incorrect, think about what the for loop will look at during the second iteration.
   :feedback_e: Incorrect, the for loop is iterating over an iterable object.
   :correct: a
   :practice: T
   :pct_on_first: 0.765470297
   :total_students_attempting: 1616
   :num_students_correct: 1603.0
   :mean_clicks_to_correct: 1.5514660012

   What’s the type of your iterator variable in the second iteration?
   
   .. sourcecode:: python
   
       t = [9, "setter", 3, "wing spiker", 10, "middle blocker"]
       for z in t:
           print(z)