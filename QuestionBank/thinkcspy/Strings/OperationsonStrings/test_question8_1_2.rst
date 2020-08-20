.. mchoice:: test_question8_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: OperationsonStrings
   :topics: Strings/OperationsonStrings
   :from_source: T
   :practice: T
   :answer_a: python!!!
   :answer_b: python!python!python!
   :answer_c: pythonpythonpython!
   :answer_d: Error, you cannot perform concatenation and repetition at the same time.
   :correct: a
   :feedback_a: Yes, repetition has precedence over concatenation
   :feedback_b: Repetition is done first.
   :feedback_c: The repetition operator is working on the excl variable.
   :feedback_d: The + and * operator are defined for strings as well as numbers.
   :pct_on_first: 0.7171458317
   :total_students_attempting: 12487
   :num_students_correct: 12432.0
   :mean_clicks_to_correct: 1.480453668

   
   What is printed by the following statements?
   
   .. code-block:: python
   
      s = "python"
      excl = "!"
      print(s+excl*3)