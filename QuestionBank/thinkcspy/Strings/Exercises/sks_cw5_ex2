.. activecode:: sks_cw5_ex2
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.1041666667
    :total_students_attempting: 96
    :num_students_correct: 68.0
    :mean_clicks_to_correct: 19.7352941176

    Write a function ``writeCrazy(theString)`` that returns a string that changes all the letters
    into alternating upper and lower case letters.  Only letters should be changed. Start the
    first letter as an upper case, and then alternate for each subsequent letter in the string.
    
    You can use the ``string`` library and use ``string.ascii_letters`` which returns a string
    of all the valid upper and lower case letters "abcdef...xyzABCD...XYZ"
    
    Ex. ``writeCrazy('Hello World 123!!')`` will return:
    
    ::
    
      HeLlO wOrLd 123!!
    
    ~~~~
    import string
    
    # define writeCrazy() function here
    
    # print out some test cases here
    print(string.ascii_letters) # you can delete this, but see what returns
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def _Crazy(self, theString):
            upper = True
            oString = ''
            for c in theString:
                if c in string.ascii_letters:
                    if upper:
                        oString = oString + c.upper()
                    else:
                        oString = oString + c.lower()            
                    upper = not upper
                else:
                    oString = oString + c
                
            return(oString)
                    
        def testOne(self):
            print('Auto-testing...')
    
            tests = [ ('HELLO this IS a TesT', 'Test 1'),
                      ('  NOW a liTTLE --1234.. harder?  ', 'Test 2') ]
                
            for t in tests:
                line = t[0]
                comment = t[1]
                self.assertEqual(writeCrazy(line), self._Crazy(line), comment)
                
    myTests().main()