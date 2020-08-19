.. activecode:: lhs_test_3_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5642857143
    :total_students_attempting: 140
    :num_students_correct: 123.0
    :mean_clicks_to_correct: 2.6016260163

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
    
            count_method = len(re.findall("[.]count", editText))
            if count_method > 0:
                self.assertEqual(count_method, 0, "Used the .count string method")
                return
        
            self.assertEqual(count("zabczdefz", "z"), 3, "Testing count")
            self.assertEqual(count("zabczdefz", "g"), 0, "Testing count")
            self.assertEqual(count("zabczdefz", "f"), 1, "Testing count")
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()