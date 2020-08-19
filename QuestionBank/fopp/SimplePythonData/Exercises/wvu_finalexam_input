.. activecode:: wvu_finalexam_input
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.4
    :total_students_attempting: 55
    :num_students_correct: 35.0
    :mean_clicks_to_correct: 1.5142857143

    Write code that asks users to enter the year they were born. Print out how many years old they will turn in 2019.
    ~~~~
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "input(" in self.getEditorText()
            self.assertEqual(test_one, True, "Prompted users.")
    
            test_two = "int(" in self.getEditorText() or "float(" in self.getEditorText()
            self.assertEqual(test_two, True, "Year in usable format.")
    
            test_three = "2019" in self.getEditorText()
            self.assertEqual(test_three, True, "2019 referenced.")
    
            test_four = "print(" in self.getEditorText()
            self.assertEqual(test_four, True, "Output to screen.")
    
    myTests().main()