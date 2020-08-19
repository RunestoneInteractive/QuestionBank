.. activecode:: RecursionTestNoTestCase
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Write the three functions described recursively. You should not have for or while loops
    in your code.

    **Problem 1:** ``count(str,ch)`` should count the number of times the single character ``ch`` is
    found in the string ``str``.

    .. sourcecode:: python

        count("hello","l") # returns 2
        count("hello","z") # returns 0


    **Problem 2** ``addDigits(n)`` returns the sum of all the digits in the integer parameter ``n``

    .. sourcecode:: python

        addDigits(123) # returns 6


    **Extra Credit**: ``reverseNum(n)`` returns an integer that is the reversal of the integer parameter ``n``

    .. sourcecode:: python

        reverseNum(1234) # return the number 4321


    ~~~~
    def count(str,ch):
        # write your code here
    
    def addDigits(str,ch):
        # write your code here
    
    def reverseNum(str,ch):
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
            
            print("Auto-Testing...")
    
            editText = self.getEditorText()
            numForWhile = len(re.findall("\s*while[( ]", editText)) + len(re.findall("\s*for ", editText))
            if numForWhile > 0:
                self.assertEqual(numForWhile, 0, "Used a for or while in code")
                return
    
            # Make an object
            self.assertEqual(count("zabczdefz", "z"), 3, "Testing count")
            self.assertEqual(count("zabczdefz", "g"), 0, "Testing count")
    
            self.assertEqual(addDigits(12345), 15, "Testing addDigits(12345)")
            self.assertEqual(addDigits(980), 17,   "Testing addDigits(980)")
    
            self.assertEqual(reverseNum(13579), 97531, "Testing reverseNum(13579)") 
            self.assertEqual(reverseNum(1203), 3021, "Testing reverseNum(1203)") 

    myTests().main()