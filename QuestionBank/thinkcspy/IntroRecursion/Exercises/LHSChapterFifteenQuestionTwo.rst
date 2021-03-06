.. activecode:: LHSChapterFifteenQuestionTwo
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

    The greatest common divisior GCD of two integers ``a`` and ``b`` is the largest
    integer ``k`` that divides both ``a`` and ``b`` evenly. (That is, ``k`` divides both
    ``a`` and ``b`` without leaving a remainder.)
    
    For example, ``gcd( 6, 9 ) == 3`` because 3 evenly divides both 6 and 9 and
    no greater integer does so. Another example, ``gcd( 25, 55 ) == 5``.
    
    Here is a math-like definition of GCD:
    
    .. sourcecode:: python
    
        gcd(0, n) = n
    
        gcd(a, b) = gcd( b % a, a )  % is the remainder after integer division b/a
    
    For example.
    
    .. sourcecode:: python
    
        gcd( 6, 9 ) = gcd( 9 % 6, 6 ) = gcd( 3, 6 )
        gcd( 3, 6 ) = gcd( 6 % 3, 3 ) = gcd( 0, 3 )
        gcd( 0, 3 ) = 3 
    
    Translate the math-like definition of gcd into a recursive Python function.
    Write a main() function to test it.     
    ~~~~
    def gcd(a, b):
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
    
            editText = self.getEditorText()
            self.assertEqual(0, len(re.findall("\s*while[( ]", editText)), "Should use no 'while' loops")
            self.assertEqual(0, len(re.findall("\s*for ", editText)), "Should use no 'for' loops")
    
            self.assertEqual(0,  gcd(0, 0), "Testing  gcd(0, 0)")
            self.assertEqual(11,  gcd(11, 0), "Testing  gcd(11, 0)")
            self.assertEqual(3,  gcd(0, 3), "Testing  gcd(0, 3)")
            self.assertEqual(3,  gcd(6, 9), "Testing  gcd(6, 9)")
            self.assertEqual(25,  gcd(25, 25), "Testing  gcd(25, 25)")
            
    myTests().main()