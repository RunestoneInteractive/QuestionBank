.. actex:: CS152_count_digit
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
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 17.0

    Write a fruitful function ``count_digit(num)`` that returns the number of digits in the integer num. Do not convert num to a string.
    
    ~~~~
    
    def count_digit(num):
        """ Returns the the number of digits in the integer num """
        # Put your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
            self.assertEqual(0, len(re.findall("\s*str", editText)), "Work with integers, not strings")
            self.assertAlmostEqual(count_digit(63),2,0,"Tested count_digit(63)")
            self.assertAlmostEqual(count_digit(6),1,0,"Tested count_digit(6)")
            self.assertAlmostEqual(count_digit(0),1,0,"Tested count_digit(0)")
            self.assertAlmostEqual(count_digit(120),3,0,"Tested count_digit(120)")
            self.assertAlmostEqual(count_digit(67589),5,0,"Tested count_digit(67589)")
            self.assertAlmostEqual(count_digit(-36),2,0,"Tested count_digit(-36)")
    
    
    
    
    myTests().main()