.. activecode:: lhs_6_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.3104265403
    :total_students_attempting: 422
    :num_students_correct: 404.0
    :mean_clicks_to_correct: 7.3242574257

    Write a function called ``listCount`` that takes as input a list and returns a count of how many items are in the list.
    
    So, for example, ``listCount(['apple', 2, 'dog'])`` should return the number 3.
    
    Use a single ``for`` loop.  (Do not use any special list function that counts the list.)
    
    ~~~~
    # My Name:
    
    def listCount(myList):
        # write your code here
        # remember 'for loopVarName in listName:' is the syntax for a for loop
    
    # Here is some code to test out your function that has been written for you
    print(listCount( [1, 2, 3, 4, 5, 6] ))   # should print out 6
    print(listCount( ['joe', 'delphina', 3.14159]))   # should print out 3 
    
    # Add any other test code you'd like below to further test out your function
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
           
        # regExString is checked inside inString
        # howMany - how many matches are expected
        # matchString - summary of what is being matched
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
    
            l = range(10)
            self.assertEqual(10, listCount(l), "List of 10")
            self.assertEqual(0, listCount([]), "Empty List")
            self.regExCheck("len\s*\(", code, 0, "len()", "Cannot use len() function")
            self.regExCheck("^\s+for .*in.*:", code, 1, "'for' loop", "Check for single 'for'")
    
    myTests().main()