.. activecode:: wvu_finalexam_averagelist
    :author: Brian Powell
    :difficulty: 1.0942436412
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.2
    :total_students_attempting: 55
    :num_students_correct: 25.0
    :mean_clicks_to_correct: 2.6

    Write a function named **average** that accepts a list as a parameter. It must return the average of all the numbers in the list.
    
    ~~~~
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "def average(" in self.getEditorText()
            self.assertEqual(test_one, True, "Function defined.")
    
            self.assertEqual(average([50,100]), 75.0, "Function gives correct result for [50, 100].")
    
    myTests().main()