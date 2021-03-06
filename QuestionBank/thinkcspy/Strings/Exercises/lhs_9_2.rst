.. activecode:: lhs_9_2
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0738095238
    :total_students_attempting: 420
    :num_students_correct: 395.0
    :mean_clicks_to_correct: 21.964556962

    Write a function ``removeSpaces(theString)`` which removes all leading and trailing spaces in a string
    and returns the stripped out string.  The string may have multiple words.
    
    You may not use the built-in string method ``.strip`` 
    
    ~~~~
    # My Name:
    
    def removeSpaces(theString):
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
                tests = [ ('    test1 case'  , 'Testing leading spaces'),
                          ('test2    '       , 'Testing trailing spaces'),
                          ('    test case3  ', 'Testing both leading & trailing spaces') ]
                
                for t in tests:
                    s = t[0]
                    comment = t[1]
                    self.assertEqual(removeSpaces(s), s.strip(), comment)
    
    myTests().main()