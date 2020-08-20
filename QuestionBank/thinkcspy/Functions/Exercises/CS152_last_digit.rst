.. actex:: CS152_last_digit
    :author: John Cigas
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 6
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 3.5

    Write a fruitful function ``last_digit(num)`` that returns the last digit (one's place) of the integer num. You do not need a loop. Do not convert num to a string.
    
    ~~~~
    
    def last_digit(num):
        """ Returns the last digit (one's place) of the integer num """
        # Put your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
            self.assertEqual(0, len(re.findall("\s*str", editText)), "Work with integers, not strings")
            self.assertAlmostEqual(last_digit(63),3,0,"Tested last_digit(63)")
            self.assertAlmostEqual(last_digit(6),6,0,"Tested last_digit(6)")
            self.assertAlmostEqual(last_digit(0),0,0,"Tested last_digit(0)")
            self.assertAlmostEqual(last_digit(120),0,0,"Tested last_digit(120)")
            self.assertAlmostEqual(last_digit(67589),9,0,"Tested last_digit(67589)")
            self.assertAlmostEqual(last_digit(-36),6,0,"Tested last_digit(-36)")
    
    
    
    
    myTests().main()