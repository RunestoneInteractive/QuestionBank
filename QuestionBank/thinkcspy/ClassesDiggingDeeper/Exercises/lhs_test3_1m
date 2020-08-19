.. activecode:: lhs_test3_1m
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 19
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    **(10pts)** Write **recursively** a function ``count(str,ch)`` which counts the 
    number of times the single character ``ch`` is found in the string ``str``.
    
    .. sourcecode:: python
    
        count("hello","l") # returns 2
        count("hello","z") # returns 0
    
    ~~~~
    
    def count(str,ch):
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
    
            count_method = len(re.findall("[.]count", editText))
            if count_method > 0:
                self.assertEqual(count_method, 0, "Used the .count string method")
                return
        
            self.assertEqual(count("zabczdefz", "z"), 3, "Testing count")
            self.assertEqual(count("zabczdefz", "g"), 0, "Testing count")
            self.assertEqual(count("zabczdefz", "f"), 1, "Testing count")
    
    myTests().main()