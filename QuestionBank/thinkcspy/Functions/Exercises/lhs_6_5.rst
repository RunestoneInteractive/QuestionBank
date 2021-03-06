.. activecode:: lhs_6_5
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5846153846
    :total_students_attempting: 455
    :num_students_correct: 450.0
    :mean_clicks_to_correct: 3.3888888889

    Write a fruitful function ``sumTo(n)`` that returns the sum of all integer numbers up to and
    including `n`.   So ``sumTo(10)`` would be ``1+2+3...+10`` which would return the value 55.  
    
    Use the equation (n * (n + 1)) / 2. 
    
    Do **not** use any loops to add up the sum.
    
    ~~~~
    
    def sumTo(n):
        # your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        # regExString - is checked inside inString
        # howMany - how many matches are expected
        # matchString - summary of what is being matched (readable version of regExString)
        # errorString - error string upon assertion failure
        def regExCheck(self, regExString, inString, howMany, matchString, errorString):
            res = re.findall(regExString, inString, re.M)
            checkOK = (len(res) == howMany)
            if not checkOK:
                print("Found [", matchString, "]", len(res), "time(s), not", howMany)
    
            self.assertEqual(checkOK, True, errorString)
    
        def testOne(self):
            print("Auto-testing...")
            outText = self.getOutput()
            code = self.getEditorText()
            
            # strips the test code - when testing code with the test code 
            pos = code.find("class myTests")
            if (pos != -1):
                code = code[:pos]
    
            if (sumTo(3) == None):
                self.assertNotEqual(sumTo(3), None, "Function is not returning anything...")
                return
    
            self.regExCheck("(?:n\s*\+\s*1)|(?:\/\s*2)", code, 2, "n+1 and /2", "Should be using formula")
    
            self.assertAlmostEqual(sumTo(15),120.0,0,"Tested sumTo on input 15")
            self.assertAlmostEqual(sumTo(0),0.0,0,"Tested sumTo on input 0")
            self.assertAlmostEqual(sumTo(25),325.0,0,"Tested sumTo on input 25")
            self.assertAlmostEqual(sumTo(7),28.0,0,"Tested sumTo on input 7")
    
    myTests().main()