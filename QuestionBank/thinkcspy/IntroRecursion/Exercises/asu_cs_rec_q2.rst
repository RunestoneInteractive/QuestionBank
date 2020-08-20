.. activecode:: asu_cs_rec_q2
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.3846153846
    :total_students_attempting: 13
    :num_students_correct: 9.0
    :mean_clicks_to_correct: 3.5555555556

    Write a **recursive** function ``maxnum(lst)`` that
    ``lst`` is a list of numbers, and the function returns
    the maximum of these numbers. You should not use the built-in ``max()`` function.
    
    Hint: Compare the first number to the maximum of the rest of the numbers. If greater, return it
    as the maximum, otherwise return the maximum of the remaining numbers in the list as the maximum.
    
    ~~~~
    def maxnum(lst):
        # Your code here
    
    def main():
        # Your test code here, next example returns 7.
        print(maxnum([3,4,1,5,6,7]))
    
    if __name__ == "__main__":
        main()
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
            print('Auto-testing...')
    
            code = self.getEditorText()
            self.assertEqual(self.getEditorText().count('max('), 0, 'You cannot use max()')
            if self.getEditorText().count('max(') != 0:
                return
    
            self.assertGreaterEqual(self.getEditorText().count('maxnum('), 3, 'Make sure you have recursive calls')
            if self.getEditorText().count('maxnum(') < 3:
                return
    
            tests = [
                 ([0,1,5,3],5,'maxnum({})->{}'),
                 ([1,3,5,-4,7,-1],7,'maxnum({})->{}'),
                 ([0],0,'maxnum({})->{}')
            ]
    
            for t in tests:
                self.assertEqual(maxnum(t[0]), t[1], t[2].format(t[0],t[1]) )
    
    myTests().main()