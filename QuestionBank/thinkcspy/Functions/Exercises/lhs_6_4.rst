.. activecode:: lhs_6_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5645514223
    :total_students_attempting: 457
    :num_students_correct: 453.0
    :mean_clicks_to_correct: 3.353200883

    Write a function ``areaOfCircle(r)`` which **returns** the area of a circle of radius ``r`` where ``r`` is a floating point or integer datatype.  Make sure you use the math module in your solution.
    ~~~~
    
    def areaOfCircle(r):
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
                print("Found [", matchString, "]", len(res), "times")
    
            self.assertEqual(checkOK, True, errorString)
    
        def testOne(self):
            print("Auto-testing...")
            outText = self.getOutput()
            code = self.getEditorText()
            
            # strips the test code - when testing code with the test code 
            pos = code.find("class myTests")
            if (pos != -1):
                code = code[:pos]
    
            #self.assertAlmostEqual(areaOfCircle(5.0),78.53981633974483,5,"Tested input: areaOfCircle(5.0)")
            self.assertEqual(areaOfCircle(5.0),78.53981633974483,"Tested input: areaOfCirlce(5.0)")
            self.assertEqual(areaOfCircle(0),0.0,"Tested input: areaOfCirlce(0)")
            self.assertAlmostEqual(areaOfCircle(31415.926535897932),3100627668.0299816,5,"Tested input: areaOfCirlce(31415.926535897932)")
            self.regExCheck("math\.pi", code, 1, "math.pi", "Should be using math.pi in calculations")
    
    
    myTests().main()