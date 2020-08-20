.. activecode:: lhs_9_6
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0618811881
    :total_students_attempting: 404
    :num_students_correct: 378.0
    :mean_clicks_to_correct: 19.2037037037

    
    Write a function called ``genAvg(numList, precision)`` that takes in a list numbers and finds the
    average of the numbers. It will then return a string that says something like:
    
    ::
    
      The average is 1.234
    
    The output format of the average is specified by the ``precision`` parameter that is given to the function.
    The parameter defines how many digits to the right of the decimal place to round to. So, if
    the precision is 2, then the output format will round to the hundredths.
    This parameter will be an integer greater or equal to 0.
    
    Use the .format method of strings to make this output string. You may need to create an initial string
    with some string concatenation operations before using the .format method since the precision 
    is not a fixed value.
    
    Example: ``genAvg([1,2,5], 4)`` will return the string ``The average is 2.6667``
    
    ~~~~
    # My Name:
    
    # define genAvg() function here
    
    # print out some test cases here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def _gen(self, listNum, precision):
            count = 0
            total = 0
            for i in listNum:
                count = count + 1
                total = total + i
            average = total / count
            formatString = 'The average is {:.' + str(precision) + 'f}'
            return(formatString.format(average))
                    
        def testOne(self):
            print('Auto-testing...')
            editText = self.getEditorText()
            Found = len(re.findall("\.format", editText)) != 0
            if Found != True:
                self.assertEqual(Found, True, "Should be using .format string method")
            else: 
                tests = [ ( [1,2,3,4,5,7] ,             5, 'Test 1'),
                          ( [1,2,3,4,5,9,17] ,          5, 'Test 2'),
                          ( [1.2 ,2.3,3,4.47, 6, 7, 8], 8, 'Test 3') ]
                    
                for t in tests:
                    n = t[0]
                    p = t[1]
                    c = t[2]
                    self.assertEqual(genAvg(n, p), self._gen(n, p), c)
                
    myTests().main()