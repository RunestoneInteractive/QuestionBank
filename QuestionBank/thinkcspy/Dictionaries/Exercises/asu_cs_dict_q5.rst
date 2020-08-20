.. activecode:: asu_cs_dict_q5
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.25
    :total_students_attempting: 12
    :num_students_correct: 8.0
    :mean_clicks_to_correct: 1.875

    Write a program that given a dictionary:
    
    ``dd = { 'joe': 100, 'jane': 80, 'don': 90, 'marry': 60 }``
    
    Find the average score of students in the dictionary and print as follows:
    
    82.5
    
    
    ~~~~
    dd = { 'joe': 100, 'jane': 80, 'don': 90, 'marry': 60 }
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
            
            dd = { 'joe': 100, 'jane': 80, 'don': 90, 'marry': 60 }
            avg = sum(dd.values())/len(dd)
                
            self.assertEqual(str(avg)+'\n', outText, "Check output...")
        
    myTests().main()