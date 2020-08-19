.. activecode:: lhs_9_t2_p6
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.25
    :total_students_attempting: 16
    :num_students_correct: 8.0
    :mean_clicks_to_correct: 2.375

    Write a function ``count_hi(str, caseSensitive)`` which **returns** a count of the number of times
    ``hi`` appears anywhere in the given string. ``caseSensitive`` is a Boolean where when
    True does a case sensitive comparison, but if False, will be case insensitive.
    
    You may **NOT** use the ``.count`` method. If you do use the ``.count`` method, you receive only 50% credit.
    
    ::
    
      count_hi('abc hi ho', True)  returns a 1
      count_hi('ABCHi hi', False)  returns a 2
    
    ~~~~
    # My Name: 
    def count_hi(str, caseSensitive):
        # Write your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _count(self, str, caseSensitive):
            word = 'hi'
            count = 0
            ## Loop to length-1 and access index i and i+1
            ## in the loop.
            for i in range(len(str)-len(word)+1):
                if caseSensitive:
                    if str[i:i+len(word)] == word:
                        count += 1
                else:
                    if str[i:i+len(word)].lower() == word:
                        count += 1    
            return count
    
        def testOne(self):
            print('Auto-testing...')
    
            tests = [ ('hi hi hi ', False),
                      (' Hi iH hI', True),
                      ('HiiHIHIhi', False),
                      ('hiHihIHI', True),
                      ('H', False),
                      ('',  True) ]
    
            for t in tests:
                self.assertEqual(count_hi(t[0], t[1]), self._count(t[0], t[1]), 'testing |' + t[0] + '| ' + str(t[1]) )
    
    
    myTests().main()