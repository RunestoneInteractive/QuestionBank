.. mchoice:: test_question8_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Length
   :topics: Strings/Length
   :from_source: T
   :practice: T
   :answer_a: o
   :answer_b: r
   :answer_c: s
   :answer_d: Error, len(s) is 12 and there is no index 12.
   :correct: b
   :feedback_a: Take a look at the index calculation again, len(s)-5.
   :feedback_b: Yes, len(s) is 12 and 12-5 is 7.  Use 7 as index and remember to start counting with 0.
   :feedback_c: s is at index 11
   :feedback_d: You subtract 5 before using the index operator so it will work.
   :pct_on_first: 0.7200321085
   :total_students_attempting: 11212
   :num_students_correct: 11140.0
   :mean_clicks_to_correct: 1.4190305206

   
   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python rocks"
      print(s[len(s)-5])