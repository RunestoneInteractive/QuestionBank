.. activecode:: wvu_finalexam_gradedecision
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Files
    :subchapter: Exercises
    :topics: Files/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1590909091
    :total_students_attempting: 44
    :num_students_correct: 16.0
    :mean_clicks_to_correct: 2.25

    Assume that the final grade for a course is determined based on this scale - A: 900+ points, B: 800-899 points, C: 700-799 points, D: 600-699 points, F: 599 or fewer points.
    
    Write a function named **get_letter_grade()** that takes the number of points the student has earned as a parameter. It should return a string containing (only) the letter grade the student will receive.
    ~~~~
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "def get_letter_grade(" in self.getEditorText()
            self.assertEqual(test_one, True, "Function defined.")
    
            self.assertEqual(get_letter_grade(1000), 'A', 'Correct grade for 1000 points.')
            self.assertEqual(get_letter_grade(700), 'C', 'Correct grade for 700 points.')
            self.assertEqual(get_letter_grade(599), 'F', 'Correct grade for 599 points.')
    
    myTests().main()