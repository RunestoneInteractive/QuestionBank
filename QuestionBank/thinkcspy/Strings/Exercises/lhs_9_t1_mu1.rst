.. activecode:: lhs_9_t1_mu1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Write a function ``doubleChar(str)`` which **returns** a string where for every
    character in the original string, there are two characters.
    
    Example:
    
    ::
    
        doubleChar('The') returns 'TThhee'
        doubleChar('AAbb') returns 'AAAAbbbb'
    
    ~~~~
    # My Name:
    def doubleChar(str):
    rite your code here
    
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _d(self, str):
            dblStr = ''
            for ch in str:
                dblStr = dblStr + ch + ch
            return dblStr
    
        def testOne(self):
            print('Auto-testing...')
    
            tests = [ 'abc',
                      'a BB  cccc\n !.',
                      '' ]
    
            for t in tests:
                self.assertEqual(doubleChar(t), self._d(t), 'testing |' + t +'|')
    
    
    myTests().main()