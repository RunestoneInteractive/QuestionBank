.. mchoice:: question6_4_2
   :author: bmiller
   :difficulty: 2.5981308411
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Stringsandforloops
   :topics: Iteration/Stringsandforloops
   :from_source: T
   :answer_a: 4
   :answer_b: 5
   :answer_c: 6
   :answer_d: Error, the for statement cannot use slice.
   :correct: b
   :feedback_a: Slice returns a sequence that can be iterated over.
   :feedback_b: Yes, The blank is part of the sequence returned by slice.
   :feedback_c: Check the result of s[3:8]. It does not include the item at index 8.
   :feedback_d: Slice returns a sequence.
   :practice: T
   :pct_on_first: 0.6004672897
   :total_students_attempting: 2140
   :num_students_correct: 2127.0
   :mean_clicks_to_correct: 1.5340855665

   How many times is the word HELLO printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      for ch in s[3:8]:
         print("HELLO")