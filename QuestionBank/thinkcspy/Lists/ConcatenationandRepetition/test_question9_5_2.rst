.. mchoice:: test_question9_5_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: ConcatenationandRepetition
   :topics: Lists/ConcatenationandRepetition
   :from_source: T
   :practice: T
   :answer_a: 9
   :answer_b: [1, 1, 1, 3, 3, 3, 5, 5, 5]
   :answer_c: [1, 3, 5, 1, 3, 5, 1, 3, 5]
   :answer_d: [3, 9, 15]
   :correct: c
   :feedback_a: Repetition does not multiply the lengths of the lists.  It repeats the items.
   :feedback_b: Repetition does not repeat each item individually.
   :feedback_c: Yes, the items of the list are repeated 3 times, one after another.
   :feedback_d: Repetition does not multiply the individual items.
   :pct_on_first: 0.8422715489
   :total_students_attempting: 12344
   :num_students_correct: 12293.0
   :mean_clicks_to_correct: 1.2494102335

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [1, 3, 5]
     print(alist * 3)