.. activecode:: asu_cs_ch04_ex1
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0526315789
    :total_students_attempting: 19
    :num_students_correct: 8.0
    :mean_clicks_to_correct: 7.375

    Write a program that given a number x (e.g. 5), prints the following:
    
    ::
    
      1 2 3 4 5
      5 4 3 2 1
    
    Use two ``for`` loops and two ``range`` functions.
    
    Hint: Use ``print(...., end=' ')`` to print in the same line.
    ~~~~
    x = 6
    # write your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        # counts how many lines have 'keyword' in word position 'where'
        def count_code(self, code, keyword, where):
            cnt = 0
            for line in code.splitlines():
                word = line.split()
                if where < len(word):
                    # parse function keyword
                    if '(' in word[where]:
                        word = word[where].split('(')
                        if word[0] == keyword:
                            cnt = cnt + 1
                    else:
                        if word[where] == keyword:
                            cnt = cnt + 1
            return(cnt)
    
        def testMany(self):
            outText = self.getOutput()
            editText = self.getEditorText()
            
            pos = editText.index('x = ')
            x = int(editText[pos + 4: pos + 5])
            out = ''
    
            for i in range(x):
               out += str(i+1) + ' '
            out += '\n'
            for i in range(x,0,-1):
               out += str(i) + ' '
    
                
            # self.assertEqual(editText.count('for'), 2, "You need to use just two 'for' loops!")
            self.assertEqual(2, self.count_code(editText, 'for', 0), "You need to use just two 'for' loops!")
            self.assertEqual(2, editText.count('range'), "You need to use just two range functions!")
            self.assertIn(out, outText, "Your output is not right for x=" + str(x))
        
    myTests().main()