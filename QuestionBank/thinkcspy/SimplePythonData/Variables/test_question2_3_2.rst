.. mchoice:: test_question2_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Variables
   :topics: SimplePythonData/Variables
   :from_source: T
   :practice: T
   :answer_a: Nothing is printed. A runtime error occurs.
   :answer_b: Thursday
   :answer_c: 32.5
   :answer_d: 19
   :correct: d
   :feedback_a: It is legal to change the type of data that a variable holds in Python.
   :feedback_b: This is the first value assigned to the variable day, but the next statements reassign that variable to new values.
   :feedback_c: This is the second value assigned to the variable day, but the next statement reassigns that variable to a new value.
   :feedback_d: The variable day will contain the last value assigned to it when it is printed.
   :pct_on_first: 0.7140349411
   :total_students_attempting: 23926
   :num_students_correct: 23836.0
   :mean_clicks_to_correct: 1.5218576942

   What is printed when the following statements execute?
   
   .. code-block:: python
   
     day = "Thursday"
     day = 32.5
     day = 19
     print(day)