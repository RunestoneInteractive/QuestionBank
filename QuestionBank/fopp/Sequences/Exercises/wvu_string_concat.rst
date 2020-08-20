.. activecode:: wvu_string_concat
   :author: Brian Powell
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :pct_on_first: 0.2230215827
   :total_students_attempting: 139
   :num_students_correct: 65.0
   :mean_clicks_to_correct: 3.6923076923

   We want to concatenate the elements of parts into a new variable named wv. Include spaces between each part.
   ~~~~
   parts = ["West Virginia was created in",
            1863,
            "when 50 counties broke away from Virginia. Today there are",
            "55",
            "counties in the state."]
   
   # Create a variable named wv containing the concatenated string
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(wv,"West Virginia was created in 1863 when 50 counties broke away from Virginia. Today there are 55 counties in the state.","Your string isn't concatenated as expected.")
   
   myTests().main()