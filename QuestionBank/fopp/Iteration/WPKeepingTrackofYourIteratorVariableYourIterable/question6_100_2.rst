.. mchoice:: question6_100_2
   :author: bmiller
   :difficulty: 1.6920332937
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
   :feedback_a: Yes, the iterable in this example is a string
   :feedback_b: Incorrect, that is not the type of the iterable.
   :feedback_c: Incorrect, that is not the type of the iterable.
   :feedback_d: Incorrect, that is not the type of the iterable.
   :feedback_e: Incorrect, Python can iterate over this type.
   :correct: a
   :practice: T
   :pct_on_first: 0.8269916766
   :total_students_attempting: 1682
   :num_students_correct: 1676.0
   :mean_clicks_to_correct: 1.3544152745

   What is the type of your iterable?
   
   .. sourcecode:: python
   
       t = "couch"
       for z in t:
           print(z)