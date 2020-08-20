.. activecode:: lhs_5_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: Exercises
    :topics: PythonModules/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0363321799
    :total_students_attempting: 578
    :num_students_correct: 416.0
    :mean_clicks_to_correct: 13.9735576923

    The iterative sequence ``1 + 1/2**2 + 1/3**2 + ... + 1/n**2`` can be used to calculate **pi** for any given ``n``. 
    
    This sum converges to ``pi**2/6`` as ``n`` increases. You will need to take the sum that you just calculated and then use it to solve for pi. This will require some basic algebraic manipulation.
    
    Write a program using a ``for`` loop and 1 million iterations (``n`` = 1000000) to compute an approximation for **pi** and then print that value as well as Python's value of ``math.pi``.
    The output of the problem should look like:
    
    
    ::
    
      After 1000000 iterations pi = 3.141591xxxxx
      Python's math.pi = 3.14159265359
    
    ~~~~
    # My Name:
    
    # write your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def regExCheck(self, regExString, inString, howMany, errorString):
            res = re.findall(regExString, inString, re.M)
            checkOK = (len(res) == howMany)
            if not checkOK:
                print("Failed to find: [" + regExString + "]")
    
            self.assertEqual(checkOK, True, errorString)
    
        def testOne(self):
            print("Auto-testing...")
            outText = self.getOutput()
            code = self.getEditorText()
    
            # return if these basic checks failed
            if not(code.find("3.141591698") == -1 and code.find("3.14159265359") == -1):
                # No hard coded answers
                self.assertNotIn("3.141591698", code, "Checking no hard coded output of answer")
                self.assertNotIn("3.14159265359", code, "Checking no hard coded output of answer")
                return
    
            # Code requriement 
            self.regExCheck("^for ", code, 1, "Checking that 'for' loop was used")
            self.regExCheck("math.sqrt", code, 1, "Checking that 'math.sqrt' was used")
            self.regExCheck("math.pi", code, 2, "Checking that 'math.pi' was used")
    
            # Output checking
            self.regExCheck("After 1000000 iterations pi = 3.141591698", outText, 1, "Checking 1st line output")
            self.regExCheck("math.pi = 3.14159265359", outText, 1, "Checking 2nd line output")
    
    myTests().main()