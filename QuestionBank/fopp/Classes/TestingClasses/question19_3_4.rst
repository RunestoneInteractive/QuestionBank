.. mchoice:: question19_3_4
   :author: bmiller
   :difficulty: 2.1919191919
   :basecourse: fopp
   :chapter: Classes
   :subchapter: TestingClasses
   :topics: Classes/TestingClasses
   :from_source: T
   :practice: T
   :answer_a: return value test
   :answer_b: side effect test
   :correct: b
   :feedback_a: The sort method always returns None, so there's nothing to check about whether it is returning the right value.
   :feedback_b: You want to check whether it has the correct side effect, whether it correctly mutates the list.
   :pct_on_first: 0.702020202
   :total_students_attempting: 396
   :num_students_correct: 393.0
   :mean_clicks_to_correct: 1.3053435115

   We have usually used the ``sorted`` function, which takes a list as input and returns a new list containing the same items, possibly in a different order. There is also a method called ``sort`` for lists (e.g. ``[1,6,2,4].sort()``). It changes the order of the items in the list itself, and it returns the value ``None``. Which kind of test case would you use on the sort method?