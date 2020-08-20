.. mchoice:: question2_6_1
   :author: bmiller
   :difficulty: 2.3194070081
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: ConvertTypeFunctions
   :topics: SimplePythonData/ConvertTypeFunctions
   :from_source: T
   :answer_a: Nothing is printed. It generates a runtime error.
   :answer_b: 53
   :answer_c: 54
   :answer_d: 53.785
   :correct: b
   :feedback_a: The statement is valid Python code.  It calls the int function on 53.785 and then prints the value that is returned.
   :feedback_b: The int function truncates all values after the decimal and prints the integer value.
   :feedback_c: When converting to an integer, the int function does not round.
   :feedback_d: The int function removes the fractional part of 53.785 and returns an integer, which is then printed.
   :practice: T
   :pct_on_first: 0.670148248
   :total_students_attempting: 2968
   :num_students_correct: 2956.0
   :mean_clicks_to_correct: 1.548037889

   What value is printed when the following statement executes?
   
   .. code-block:: python
   
      print(int(53.785))