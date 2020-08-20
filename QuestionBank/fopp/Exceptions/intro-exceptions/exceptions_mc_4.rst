.. mchoice:: exceptions_mc_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: intro-exceptions
   :topics: Exceptions/intro-exceptions
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 3
   :answer_d: 4
   :answer_e: 5
   :feedback_a: Try i = 0; that should print out .3333
   :feedback_b: Keep trying.
   :feedback_c: When i=3, it will no longer be able to pring 1.0/ (3-i), but it will still print one more line in the except clause.
   :feedback_d: It will print the fraction for three values of i, and then one error message.
   :feedback_e: When i=3, it will get a run-time error, and execution stops after that.
   :correct: d
   :practice: T
   :pct_on_first: 0.2908496732
   :total_students_attempting: 306
   :num_students_correct: 301.0
   :mean_clicks_to_correct: 2.4684385382

   How many lines will print out when the following code is executed?
   
   .. sourcecode:: python
   
      try:
          for i in range(5):
              print(1.0 / (3-i))
      except Exception as error_inst:
          print("Got an error", error_inst)