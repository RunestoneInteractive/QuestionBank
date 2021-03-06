.. activecode:: RecursionTest1
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 20.0

    Write the three functions described recursively. You should not have for or while loops
    in your code.
    
    **Problem 1:** ``count(str,ch)`` should count the number of times the single character ``ch`` is
    found in the string ``str``.
    
    .. sourcecode:: python
    
        count("hello","l") # returns 2
        count("hello","z") # returns 0
    
    
    **Problem 2** ``addDigits(n)`` returns the sum of all the digits in the integer parameter ``n``.
    **Hint**... the mod operator and the integer divide are your friends...
    
    .. sourcecode:: python
    
        addDigits(123) # returns 6
    
    
    **Extra Credit**: ``reverseNum(n)`` returns an integer that is the reversal of the integer parameter ``n``
    
    .. sourcecode:: python
    
        reverseNum(1234) # returns the number 4321
    
    
    ~~~~
    def count(str,ch):
        # write your code here
    
    def addDigits(n):  
        # n is an integer
        # write your code here
    
    def reverseNum(n): 
        # n is an integer
        # write your code here
    
    # Make your own test cases here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            editText = self.getEditorText()
            numForWhile = len(re.findall("\s*while[( ]", editText)) + len(re.findall("\s*for ", editText))
            if numForWhile > 0:
                self.assertEqual(numForWhile, 0, "Used a for or while in code")
                return
    
            count_method = len(re.findall("[.]count", editText))
            if count_method > 0:
                self.assertEqual(count_method, 0, "Used the .count string method")
                return
            print("Auto-Testing...")
            # Make an object
            self.assertEqual(count("zabczdefz", "z"), 3, "Testing count")
            self.assertEqual(count("zabczdefz", "g"), 0, "Testing count")
    
            self.assertEqual(addDigits(12345), 15, "Testing addDigits(12345)")
            self.assertEqual(addDigits(980), 17,   "Testing addDigits(980)")
    
            extra_credit = (reverseNum(13579) == 97531) and (reverseNum(1203) == 3021)
            self.assertEqual(extra_credit, True, "Extra credit problem working")
    
    myTests().main()