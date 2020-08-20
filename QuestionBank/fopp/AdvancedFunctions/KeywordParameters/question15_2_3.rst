.. mchoice:: question15_2_3
   :author: bmiller
   :difficulty: 3.501216545
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: KeywordParameters
   :topics: AdvancedFunctions/KeywordParameters
   :from_source: T
   :answer_a: 2
   :answer_b: 3
   :answer_c: 5
   :answer_d: 7
   :answer_e: Runtime error since two different values are provided for x
   :correct: e
   :feedback_a: 2 is bound to x since it's the first value, but so is 5, based on keyword.
   :feedback_b: 
   :feedback_c: 5 is bound to x by keyword, but 2 is also bound to it by virtue of being the value and not having a keyword. In the online environment, it actually allows this, but not in a proper python interpreter.
   :feedback_d: 
   :feedback_e: 2 is bound to x since it's the first value, but so is 5, based on keyword.
   :practice: T
   :pct_on_first: 0.3746958637
   :total_students_attempting: 411
   :num_students_correct: 398.0
   :mean_clicks_to_correct: 2.3844221106

   What value will be printed for x?
   
   .. code-block:: python
   
      initial = 7
      def f(x, y = 3, z = initial):
          print("x, y, z are:", x, y, z)
   
      f(2, x=5)