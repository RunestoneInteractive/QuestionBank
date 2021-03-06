.. activecode:: lhs_test_3_2
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5815602837
    :total_students_attempting: 141
    :num_students_correct: 125.0
    :mean_clicks_to_correct: 3.488

    **(5 pts)** Write **recursively** a function ``addDigits(n)`` which returns the 
    sum of all the digits in the **integer** parameter ``n``
    
    **HINT:** The ``%`` and ``//`` operators will be useful.
    
    .. sourcecode:: python
    
        addDigits(123) # returns integer 6
    
    ~~~~
    
    def addDigits(n):
        # write your code here
    
    # Make your own test cases here
    
    ====
    import re
    import sys
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            editText = self.getEditorText()
            numForWhile = len(re.findall("\s*while[( ]", editText)) + len(re.findall("\s*for ", editText))
            if numForWhile > 0:
                self.assertEqual(numForWhile, 0, "Used a for or while in code")
                return
    
            self.assertEqual(addDigits(12345), 15, "Testing addDigits(12345)")
            self.assertEqual(addDigits(980), 17,   "Testing addDigits(980)")
            self.assertEqual(addDigits(908), 17,   "Testing addDigits(908)")
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()