.. mchoice:: question15_2_2
   :author: bmiller
   :difficulty: 2.1207729469
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: KeywordParameters
   :topics: AdvancedFunctions/KeywordParameters
   :from_source: T
   :answer_a: 2
   :answer_b: 3
   :answer_c: 5
   :answer_d: 10
   :answer_e: Runtime error since no value is provided for y, which comes before z
   :correct: b
   :feedback_a: 2 is bound to x, not y
   :feedback_b: 3 is the default value for y, and no value is specified for y,
   :feedback_c: say what?
   :feedback_d: 10 is the second value passed, but it is bound to z, not y.
   :feedback_e: That's the beauty of passing parameters with keywords; you can skip some parameters and they get their default values.
   :practice: T
   :pct_on_first: 0.7198067633
   :total_students_attempting: 414
   :num_students_correct: 409.0
   :mean_clicks_to_correct: 1.4180929095

   What value will be printed for y?
   
   .. code-block:: python
   
      initial = 7
      def f(x, y = 3, z = initial):
          print("x, y, z are:", x, y, z)
   
      f(2, z = 10)