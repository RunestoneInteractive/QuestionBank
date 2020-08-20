.. actex:: ex_5_7_PT
    :author: pranoj thapa
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :pct_on_first: 0.5833333333
    :total_students_attempting: 12
    :num_students_correct: 11.0
    :mean_clicks_to_correct: 3.2727272727

    Write a fruitful function ``sumTo(n)`` that returns the sum of all integer numbers up to and
    including `n`.   So ``sumTo(10)`` would be ``1+2+3...+10`` which would return the value 55.  Use the
    equation  (n * (n + 1)) / 2.
    ~~~~
    
    def sumTo(n):
        # your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
            self.assertAlmostEqual(sumTo(1),1.0,0,"Tested sumTo on input 1")
            self.assertAlmostEqual(sumTo(15),120.0,0,"Tested sumTo on input 15")
            self.assertAlmostEqual(sumTo(0),0.0,0,"Tested sumTo on input 0")
            self.assertAlmostEqual(sumTo(25),325.0,0,"Tested sumTo on input 25")
            self.assertAlmostEqual(sumTo(7),28.0,0,"Tested sumTo on input 7")
            self.assertAlmostEqual(sumTo(100),5050.0,0,"Tested sumTo on input 100")
            
         
    
    myTests().main()