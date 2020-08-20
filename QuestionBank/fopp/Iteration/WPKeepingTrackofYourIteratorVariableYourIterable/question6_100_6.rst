.. mchoice:: question6_100_6
   :author: bmiller
   :difficulty: 4.0422535211
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
   :feedback_a: Correct! Every item in the iterator variable will be a string.
   :feedback_b: Incorrect, that is not the type of the iterator variable.
   :feedback_c: Incorrect, that is not the type of the iterator variable.
   :feedback_d: Incorrect, that is not the type of the iterator variable.
   :feedback_e: Incorrect, the for loop is iterating over an iterable object.
   :correct: a
   :practice: T
   :pct_on_first: 0.2394366197
   :total_students_attempting: 1633
   :num_students_correct: 1623.0
   :mean_clicks_to_correct: 2.741836106

   What’s the type of your iterator variable?
   
   .. sourcecode:: python
   
       t = ["couch", "chair", "washer", "dryer", "table"]
       for z in t:
           print(z)