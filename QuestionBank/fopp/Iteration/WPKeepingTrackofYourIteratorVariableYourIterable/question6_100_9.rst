.. mchoice:: question6_100_9
   :author: bmiller
   :difficulty: 3.0
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
   :feedback_a: Yes, the last value stored in the iterator variable is a string.
   :feedback_b: Incorrect, there is no list in the code.
   :feedback_c: Incorrect, there is no tuple in the code.
   :feedback_d: Incorrect, there is no integer in the code.
   :feedback_e: Incorrect, the for loop is iterating over an iterable object.
   :correct: a
   :practice: T
   :pct_on_first: 0.768
   :total_students_attempting: 1625
   :num_students_correct: 1613.0
   :mean_clicks_to_correct: 1.4724116553

   What’s the type of your iterator variable in the final iteration?
   
   .. sourcecode:: python
   
       red = "colors"
       for blue in red:
           print(blue)