.. activecode:: LHSChapterFIfteenQuestionEight
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    A palindrome is a string that is the same when reversed. For example, "abba"
    is a palindrome. Here is a math-like definition:
    
    .. sourcecode:: python
    
        palindrome( "" ) = true
    
        palindrome( x )  = true
    
        palindrome( x+X+y ) = false, if x != y
                            = palindrome( X ), if x == y
    
    The symbol ``x`` stands for a single character, as does ``y``. The symbol ``X`` stands
    for a string of characters. The symbol ``+`` stands for concatenation. To implement
    this definition, you can assume that the string parameter will consist entirely of
    alphabetic characters. However, your function should be case insensitive.
    
    Implement the recursive boolean function ``palindrome()`` and a program that tests it.
    ~~~~
    def palindrome(aString):
        # Your recursive code here
    
    def main():
        # Your test code here
    
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
    
            self.assertEqual(True, palindrome(""), 'Testing palindrome("")')
            self.assertEqual(True, palindrome("r"), 'Testing palindrome("r")')
            self.assertEqual(True, palindrome("radar"), 'Testing palindrome("radar")')
            self.assertEqual(True, palindrome("AbBa"), 'Testing palindrome("AbBa")')
            self.assertEqual(True, palindrome("madamimadam"), 'Testing palindrome("madamimadam")')
            self.assertEqual(False, palindrome("rada"), 'Testing palindrome("rada")')
            self.assertEqual(False, palindrome("zyzzx"), 'Testing palindrome("zyzzx")')
    myTests().main()