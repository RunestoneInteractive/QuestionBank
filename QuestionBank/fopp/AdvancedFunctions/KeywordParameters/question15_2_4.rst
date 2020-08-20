.. mchoice:: question15_2_4
   :author: bmiller
   :difficulty: 2.3759213759
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: KeywordParameters
   :topics: AdvancedFunctions/KeywordParameters
   :from_source: T
   :answer_a: 2
   :answer_b: 7
   :answer_c: 0
   :answer_d: Runtime error since two different values are provided for initial.
   :correct: b
   :feedback_a: 2 is bound to x, no z
   :feedback_b: the default value for z is determined at the time the function is defined; at that time initial has the value 7.
   :feedback_c: the default value for z is determined at the time the function is defined, not when it is invoked.
   :feedback_d: there's nothing wrong with reassigning the value of a variable at a later time.
   :practice: T
   :pct_on_first: 0.656019656
   :total_students_attempting: 407
   :num_students_correct: 401.0
   :mean_clicks_to_correct: 1.4713216958

   What value will be printed for z?
   
   .. code-block:: python
   
      initial = 7
      def f(x, y = 3, z = initial):
          print ("x, y, z are:", x, y, z)
      initial = 0
      f(2)