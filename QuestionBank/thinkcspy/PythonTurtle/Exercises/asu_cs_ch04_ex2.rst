.. activecode:: asu_cs_ch04_ex2
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    Write a program that given a number x (e.g. 5), prints the following:
    
    ::
    
      1 + 2 + 3 + 4 + 5 = 15
    
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
               out += str(i+1) + ' + '
            out = out[:-2] + '= ' + int(str(x * (x+1) / 2))
                
            # self.assertEqual(editText.count('for'), 2, "You need to use just two 'for' loops!")
            self.assertIn(out, outText, "Your output is not right for x=" + str(x))
        
    myTests().main()