.. mchoice:: question2_16_1
   :author: bmiller
   :difficulty: 2.8910231282
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Input
   :topics: SimplePythonData/Input
   :from_source: T
   :answer_a: &lt;class 'str'&gt;
   :answer_b: &lt;class 'int'&gt;
   :answer_c: &lt;class 18&gt;
   :answer_d: 18
   :correct: a
   :feedback_a: All input from users is read in as a string.
   :feedback_b: Even though the user typed in an integer, it does not come into the program as an integer.
   :feedback_c: 18 is the value of what the user typed, not the type of the data.
   :feedback_d: 18 is the value of what the user typed, not the type of the data.
   :practice: T
   :pct_on_first: 0.527244218
   :total_students_attempting: 2551
   :num_students_correct: 2530.0
   :mean_clicks_to_correct: 1.9612648221

   What is printed when the following statements execute?
   
   .. code-block:: python
   
     n = input("Please enter your age: ")
     # user types in 18
     print(type(n))