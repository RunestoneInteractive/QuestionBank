.. mchoice:: question5_7_2
   :author: bmiller
   :difficulty: 1.8540792541
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: ConcatenationandRepetition
   :topics: Sequences/ConcatenationandRepetition
   :from_source: T
   :answer_a: 9
   :answer_b: [1,1,1,3,3,3,5,5,5]
   :answer_c: [1,3,5,1,3,5,1,3,5]
   :answer_d: [3,9,15]
   :correct: c
   :feedback_a: Repetition does not multiply the lengths of the lists.  It repeats the items.
   :feedback_b: Repetition does not repeat each item individually.
   :feedback_c: Yes, the items of the list are repeated 3 times, one after another.
   :feedback_d: Repetition does not multiply the individual items.
   :practice: T
   :pct_on_first: 0.7864801865
   :total_students_attempting: 2145
   :num_students_correct: 2139.0
   :mean_clicks_to_correct: 1.3403459561

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [1,3,5]
     print(alist * 3)