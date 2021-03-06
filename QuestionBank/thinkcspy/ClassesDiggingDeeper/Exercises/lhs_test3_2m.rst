.. activecode:: lhs_test3_2m
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.05
    :total_students_attempting: 20
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

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
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
    
            SelfTest = True
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing is OFF - you must check the program yourself for now")
                return
    
            editText = self.getEditorText()
            numForWhile = len(re.findall("\s*while[( ]", editText)) + len(re.findall("\s*for ", editText))
            if numForWhile > 0:
                self.assertEqual(numForWhile, 0, "Used a for or while in code")
                return
    
            self.assertEqual(addDigits(12345), 15, "Testing addDigits(12345)")
            self.assertEqual(addDigits(980), 17,   "Testing addDigits(980)")
            self.assertEqual(addDigits(908), 17,   "Testing addDigits(908)")
    
    myTests().main()