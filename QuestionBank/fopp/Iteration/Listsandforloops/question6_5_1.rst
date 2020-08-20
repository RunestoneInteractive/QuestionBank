.. mchoice:: question6_5_1
   :author: bmiller
   :difficulty: 1.9828683309
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Listsandforloops
   :topics: Iteration/Listsandforloops
   :from_source: T
   :answer_a: 8
   :answer_b: 9
   :answer_c: 15
   :answer_d: Error, the for statement needs to use the range function.
   :correct: b
   :feedback_a: Iteration by item will process once for each item in the sequence, even the empty list.
   :feedback_b: Yes, there are nine elements in the list so the for loop will iterate nine times.
   :feedback_c: Iteration by item will process once for each item in the sequence. Each string is viewed as a single item, even if you are able to iterate over a string itself.
   :feedback_d: The for statement can iterate over a sequence item by item.
   :practice: T
   :pct_on_first: 0.7542829173
   :total_students_attempting: 2043
   :num_students_correct: 2033.0
   :mean_clicks_to_correct: 1.3349729464

   How many times will the for loop iterate in the following statements?
   
   .. code-block:: python
   
      p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
      for ch in p:
         print(ch)