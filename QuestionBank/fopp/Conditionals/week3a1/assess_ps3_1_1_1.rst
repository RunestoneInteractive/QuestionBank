.. activecode:: assess_ps3_1_1_1
    :author: bmiller
    :difficulty: 1.3505049003
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: week3a1
    :topics: Conditionals/week3a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.1351626016
    :total_students_attempting: 984
    :num_students_correct: 729.0
    :mean_clicks_to_correct: 6.950617284

    ``rainfall_mi`` is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma.
    Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable ``num_rainy_months``.
    In other words, count the number of items with values ``> 3.0``.
    
    
    Hard-coded answers will receive no credit.
    ~~~~
    rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
    =====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn('for', self.getEditorText(), "Testing that your code has a for loop (Don't worry about actual and expected values).")
            self.assertEqual(num_rainy_months, 5, "Testing that num_rainy_months has the right value")
    
    myTests().main()