.. mchoice:: question6_100_1
   :author: bmiller
   :difficulty: 2.8034544372
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
   :feedback_a: Incorrect, that is not the type of the iterable.
   :feedback_b: Yes, the iterable is n, and it is a list.
   :feedback_c: Incorrect, that is not the type of the iterable.
   :feedback_d: Incorrect, that is not the type of the iterable.
   :feedback_e: Incorrect, Python can iterate over this type.
   :correct: b
   :practice: T
   :pct_on_first: 0.5491363907
   :total_students_attempting: 1679
   :num_students_correct: 1670.0
   :mean_clicks_to_correct: 1.851497006

   What is the type of your iterable?
   
   .. sourcecode:: python
   
       n = ["word", "phrase", 8, ("beam")]
       for item in n:
           print(item)