.. mchoice:: question15_3_1
   :author: bmiller
   :difficulty: 1.8955223881
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: Anonymousfunctionswithlambdaexpressions
   :topics: AdvancedFunctions/Anonymousfunctionswithlambdaexpressions
   :from_source: T
   :answer_a: A string with a - in front of the number.
   :answer_b: A number of the opposite sign (positive number becomes negative, negative becomes positive).
   :answer_c: Nothing is returned because there is no return statement.
   :correct: b
   :feedback_a: The number would be assigned to the variable x and there is no type conversion used here, so the number would stay a number.
   :feedback_b: Correct!
   :feedback_c: Remember, lambda functions do not use return statements.
   :practice: T
   :pct_on_first: 0.776119403
   :total_students_attempting: 402
   :num_students_correct: 396.0
   :mean_clicks_to_correct: 1.2575757576

   If the input to this lambda function is a number, what is returned?
   
   .. code-block:: python
   
    (lambda x: -x)