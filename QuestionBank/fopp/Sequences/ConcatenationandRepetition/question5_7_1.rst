.. mchoice:: question5_7_1
   :author: bmiller
   :difficulty: 1.7325256291
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: ConcatenationandRepetition
   :topics: Sequences/ConcatenationandRepetition
   :from_source: T
   :answer_a: 6
   :answer_b: [1,2,3,4,5,6]
   :answer_c: [1,3,5,2,4,6]
   :answer_d: [3,7,11]
   :correct: c
   :feedback_a: Concatenation does not add the lengths of the lists.
   :feedback_b: Concatenation does not reorder the items.
   :feedback_c: Yes, a new list with all the items of the first list followed by all those from the second.
   :feedback_d: Concatenation does not add the individual items.
   :practice: T
   :pct_on_first: 0.8168685927
   :total_students_attempting: 2146
   :num_students_correct: 2141.0
   :mean_clicks_to_correct: 1.2344698739

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [1,3,5]
     blist = [2,4,6]
     print(alist + blist)