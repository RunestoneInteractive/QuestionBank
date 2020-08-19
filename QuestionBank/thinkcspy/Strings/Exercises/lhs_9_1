.. activecode:: lhs_9_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1057471264
    :total_students_attempting: 435
    :num_students_correct: 414.0
    :mean_clicks_to_correct: 17.7053140097

    Write a function ``removeLeftSpaces(theString)`` which removes all leading spaces in a string
    and returns the stripped out string.  The string may have multiple words.
    
    You may **not** use the built-in string method ``.lstrip`` 
    
    Ex. ``removeLeftSpaces("     Hello Joe  ")`` would return the string ``"Hello Joe  "``
    
    ~~~~
    # My Name:
    
    def removeLeftSpaces(theString):
        # write your code here
    
    # any test cases you'd like to have
    
    ====    
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            print('Auto-testing...')
    
            # Check that strip is not being used
            editText = self.getEditorText()
            Found = len(re.findall("\..?strip", editText)) != 0
            if Found == True:
                self.assertEqual(Found, False, "Should not use .strip string method")
            else: 
                tests = [ ('t est1 case '  , 'Testing 0 leading spaces'),
                          ('    test case2  ', 'Testing both leading & trailing spaces'), 
                          (' test case 3', '1 leading space with other spaces and no ending space'), 
                          ('testcase4', 'no spaces in string'), 
                          ('', 'empty string'),
                          ('     ', 'Just spaces') ]
            
                for t in tests:
                    s = t[0]
                    comment = t[1]
                    self.assertEqual(removeLeftSpaces(s), s.lstrip(), comment)
    
    myTests().main()