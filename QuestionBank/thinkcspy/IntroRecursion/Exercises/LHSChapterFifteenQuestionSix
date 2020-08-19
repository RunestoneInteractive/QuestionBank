.. activecode:: LHSChapterFifteenQuestionSix
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Write a recursive function that implements this definition of cube numbers:
    
    .. sourcecode:: python
    
        cube(1) = 1
        cube(n) = cube(n-1) + 3(square(n)) - 3n + 1
    
    Implement the recursive ``square()`` function using this definition:
    
    .. sourcecode:: python
    
        square(1) = 1
        square(n) = square(n-1) + 2n - 1
    
    Translate the math-like definitions of ``cube`` and ``square`` into recursive Python functions.
    Test your program.
    You may assume that n >= 1.
    ~~~~
    def square(n):
        # Your recursive code here
    
    def cube(n):
        #Your code here
    
    def main():
        # Your test code here
    
    if __name__ == "__main__":
        main()
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def _pascal(self, n, k):
            if k == 0 or k == n:
                return str(1)
            else:
                return str(int(self._pascal(n - 1, k - 1)) + int(self._pascal(n - 1, k)))
    
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
            print('Auto-testing...')
    
            editText = self.getEditorText()
            self.assertEqual(0, len(re.findall("\s*while[( ]", editText)), "Should use no 'while' loops")
            self.assertEqual(0, len(re.findall("\s*for ", editText)), "Should use no 'for' loops")
    
            self.assertEqual(1, square(1), "Testing square(1)")
            self.assertEqual(9, square(3), "Testing square(3)")
            self.assertEqual(1, cube(1), "Testing cube(1)")
            self.assertEqual(729, cube(square(3)), "Testing cube(square(3))")
    myTests().main()