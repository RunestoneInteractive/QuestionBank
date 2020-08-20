.. activecode:: JC3
    :author: Joaquin Carbonara
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: Exercises
    :topics: PythonModules/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.1304347826
    :total_students_attempting: 23
    :num_students_correct: 7.0
    :mean_clicks_to_correct: 2.7142857143

    Write a program using a ``for`` loop and the ``random`` module to display the results of rolling a pair of dice 10 times and adding up the results.
    
    (You must use exactly 1 ``for`` statement,  and 2 ``randrange`` statements.)
    
    ::
    
      Results from rolling a pair of dice 10 times:
      7
      8
      10
      8
      6
      3
      5
      3
      3
      5
    
    ~~~~
    # My Name:
    
    # write your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        # counts how many instances of 'keyword'
        def count_code(self, code, keyword):
            cnt = 0
            for line in code.splitlines():
                words = line.split()
                for val in words:
                    if val.find(keyword) >= 0:
                        cnt = cnt + 1
            return(cnt)
    
        def check_output(self, num):
            if len(num) != 10:
                return(False)
            for i in num:
                if (int(i) > 12) or (int(i) < 2):
                    return(False)
            return(True)
    
        def testOne(self):
            outText = self.getOutput()
            editText = self.getEditorText()
            numList = re.findall(r'^\d+$', outText, re.M)
    
            self.assertTrue(len(outText) > 0, "Comparing printed output")
            self.assertEqual(1, self.count_code(editText, 'for'), "Checking 'for' usage")
            self.assertEqual(2, len(re.findall("randrange\s*\(\s*1\s*,\s*7\s*\)", editText)), "Checking for randrange and proper parameters")
            self.assertTrue(self.check_output(numList), "Ten die pair sums should be between 2 and 12")
    
    myTests().main()