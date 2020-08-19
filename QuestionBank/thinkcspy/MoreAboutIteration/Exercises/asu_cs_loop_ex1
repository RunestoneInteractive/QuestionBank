.. activecode:: asu_cs_loop_ex1
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2142857143
    :total_students_attempting: 14
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 2.2

    Write a program that given a number x (e.g. 5), prints the following:
    
    ::
    
           *
          *
         *
        *
       *
    
    ~~~~
    x = 5
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
               out += (x-i-1)*' ' + '*\n'
                
            # self.assertEqual(editText.count('for'), 2, "You need to use just two 'for' loops!")
            # self.assertEqual(2, self.count_code(editText, 'for', 0), "You need to use just two 'for' loops!")
            # self.assertEqual(2, editText.count('range'), "You need to use just two range functions!")
            self.assertIn(out, outText, "Check output for x=" + str(x))
        
    myTests().main()