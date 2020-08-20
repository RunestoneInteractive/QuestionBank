.. activecode:: ex_2_6_jcomes
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4
    :total_students_attempting: 5
    :num_students_correct: 4.0
    :mean_clicks_to_correct: 5.25

    It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday.
    If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return
    home after 10 nights you would return home on a Saturday (day 6).
    
    Write a general version of the program which (1) prompts the user for a starting day number 
    and the length of their stay, then (2) stores the values as type ``int`` variables 
    ``start_day`` and ``stay_length`` respectively, and finally (3) prints the 
    number of the day of the week they will return in an appropriate message. 
    ~~~~
    
    ====
    from unittest.gui import TestCaseGui
    import re
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(type(start_day), type(2), 'Checking the type of the variable start_day')
            self.assertEqual(type(stay_length), type(2), 'Checking the type of the variable stay_length')
            self.assertTrue(re.search('input', self.getEditorText()), 'Checking that input is used.')
            self.assertTrue(re.search(str((start_day + stay_length) % 7), self.getOutput()), 'Checking answer.')
    myTests().main()