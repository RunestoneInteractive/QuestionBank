.. activecode:: asu_cs_recursive_q2
    :author: Erdogan Dogdu
    :difficulty: 4.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5909090909
    :total_students_attempting: 22
    :num_students_correct: 19.0
    :mean_clicks_to_correct: 1.5263157895

    Write a **recursive** function ``sumSquares(num)`` that
    given an integer ``num``, returns the sum of squares of numbers
    from 1 to num. For example: ``sumSquares(3)`` should return
    1^2 + 2^2 + 3^2 = 14.
    
    ~~~~
    def sumSquares(num):
        # Your recursive code here
    
    def main():
        # Your test code here
        print(sumSquares(3))
    
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
    
            editText = self.getEditorText()
            self.assertEqual(0, len(re.findall("\s*while[( ]", editText)), "Should use no 'while' loops")
            self.assertEqual(0, len(re.findall("\s*for ", editText)), "Should use no 'for' loops")
    
            tests = [(3,14),
                     (2,5),
                     (1,1),
                     (4,30)]
    
            for t in tests:
                self.assertEqual(sumSquares(t[0]), t[1], 'Testing sumSquares({}) is {}'.format(t[0], t[1]) )
    
    myTests().main()