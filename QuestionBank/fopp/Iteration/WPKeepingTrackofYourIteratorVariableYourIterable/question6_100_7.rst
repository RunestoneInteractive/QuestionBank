.. mchoice:: question6_100_7
   :author: bmiller
   :difficulty: 3.2674060382
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
   :feedback_a: Incorrect, think about what the for loop will look at first.
   :feedback_b: Incorrect, that is the type of the iterable, not the iterator variable.
   :feedback_c: Incorrect, there is no tuple in the code.
   :feedback_d: Yes, the first item in t is an integer.
   :feedback_e: Incorrect, the for loop is iterating over an iterable object.
   :correct: d
   :practice: T
   :pct_on_first: 0.4331484904
   :total_students_attempting: 1623
   :num_students_correct: 1613.0
   :mean_clicks_to_correct: 2.4153750775

   What’s the type of your iterator variable in the first iteration?
   
   .. sourcecode:: python
   
       t = [9, "setter", 3, "wing spiker", 10, "middle blocker"]
       for z in t:
           print(z)