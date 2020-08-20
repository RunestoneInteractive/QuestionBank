.. mchoice:: question2_3_2
   :author: bmiller
   :difficulty: 3.6378653113
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Operators
   :topics: SimplePythonData/Operators
   :from_source: T
   :answer_a: 4.5
   :answer_b: 5
   :answer_c: 4
   :answer_d: 4.0
   :answer_e: 2
   :correct: d
   :feedback_a: - // does truncated division.
   :feedback_b: - Neither / nor // leads to rounding up
   :feedback_c: - Even though it truncates, it produces a floating point result
   :feedback_d: - Yes, even though it truncates, it produces a floating point result because 18.0 is a float
   :feedback_e: - / does division. Perhaps you were thinking of %, which computes the remainder?
   :practice: T
   :pct_on_first: 0.3405336722
   :total_students_attempting: 3148
   :num_students_correct: 3118.0
   :mean_clicks_to_correct: 2.0147530468

   What value is printed when the following statement executes?
   
   .. code-block:: python
   
      print(18.0 // 4)