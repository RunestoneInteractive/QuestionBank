.. activecode:: lhs_5_3
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: Exercises
    :topics: PythonModules/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1552419355
    :total_students_attempting: 496
    :num_students_correct: 428.0
    :mean_clicks_to_correct: 7.8504672897

    Write a program that calculates the value of e using 12 terms of the following:
    
    e = sum of a_i where a_i = 1/i!
    
    Example:  3 term approximation is 1/0! + 1/1! + 1/2!
    
    Print the output as follows. Be careful with spelling and spacing.
    
    Use the math module to find the value of e. 
    
    Use exactly one ``for`` statement and one ``range`` statement in your program.
    
    **HINT**: The math library might already have a factorial function...!!!
    
    ::
    
      e approximation after 12 iterations: 2.71xxxx
      python's math.e: 2.71828182846
    
    ~~~~
    # My Name:
    
    # Write your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        # counts how many lines have 'keyword' in word position 'where'
        def count_code(self, code, keyword, where):
            cnt = 0
            for line in code.splitlines():
                word = line.split()
                if where < len(word):
                    # parse function word out when there is (
                    if '(' in word[where]:
                        word = word[where].split('(')
                        if word[0] == keyword:
                            cnt = cnt + 1
                    else:
                        if word[where] == keyword:
                            cnt = cnt + 1
            return(cnt)
    
        def testOne(self):
            outText = self.getOutput()
            editText = self.getEditorText()
            
            golden_str = ""
            e_approx = 0
            max = 12
            for i in range(max):
                e_approx = e_approx + 1 / math.factorial(i)
    
            self.assertNotIn("2.7182818262", editText, "Checking no hard coded output of answer")
            self.assertNotIn("2.71828182846", editText, "Checking no hard coded output of answer")
    
            # return if these basic checks failed
            if not(editText.find("2.7182818262") == -1 and editText.find("2.71828182846") == -1):
                return
        
            line1 = "e approximation after " + str(max) + " iterations: " + str(e_approx)
            self.assertIn(line1, outText, "Checking 1st line output")
    
            line2 = "python's math.e: " + str(math.e)
            self.assertIn(line2, outText, "Checking 2nd line output")        
    
            self.assertEqual(1, self.count_code(editText, 'for', 0), "Checking 'for' usage")
            self.assertEqual(1, self.count_code(editText, 'range', 3), "Checking 'range' usage")
        
    myTests().main()