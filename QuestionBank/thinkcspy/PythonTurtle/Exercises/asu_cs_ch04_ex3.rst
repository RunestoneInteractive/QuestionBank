.. activecode:: asu_cs_ch04_ex3
    :author: Erdogan Dogdu
    :difficulty: 4.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1052631579
    :total_students_attempting: 19
    :num_students_correct: 6.0
    :mean_clicks_to_correct: 3.0

    Write a program that given a number x (e.g. 5), prints the following:
    
    ::
    
      1 5
      2 4
      3 3
      4 2
      5 1
    
    Use one ``for`` loop and one ``range`` function.
    
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
    
            for i in range(1,x+1):
               out += str(i) + ' ' + str(x-i+1) + '\n'
            self.assertEqual(1, self.count_code(editText, 'for', 0), "You need to use just two 'for' loops!")
            self.assertEqual(1, editText.count('range'), "You need to use just two range functions!")
            self.assertIn(out, outText, "Your output is not right for x=" + str(x))
        
    myTests().main()