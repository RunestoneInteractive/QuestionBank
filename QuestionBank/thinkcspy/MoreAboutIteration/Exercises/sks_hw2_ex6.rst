.. activecode:: sks_hw2_ex6
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    
    Another amazing fact from calculus is that division can be done without using a
    divide operation. Say that you wish to divide ``A`` by ``B`` to produce ``A/B``.
    You could do this by multiplying ``A`` by the reciprocal of ``B``: ::

        A * (1/B)

    Of course, now you need the reciprocal of ``B``, but this, too, can be calculated
    without division. Say that ``x`` is your best guess about the value ``1/B``.
    Then your guess can be improved by using the formula: ::

        x' = x*(2-B*x)

    Of course, now that guess can be further improved by applying the same formula to it.
    This formula is yet another application of Newton's Method.

    For example, say that you want to calculate 1/4 and your first guess for this value
    is 0.1 (see below for a better first guess). Then an improved guess is: ::

        x' = 0.1 * (2 - 4*0.1) = 0.1 * (2 - .4) = 0.1*(1.6) = 0.16

    Then the next guess is: ::

        x' = 0.16 * (2 - 4*0.16) = 0.16 * (2 - 0.64) = 0.16 * 1.36 = 0.2176

    A further improvement is: ::

        x' = 0.2176 * (2 - 4*0.2176) = 0.2176 * (2 - 0.8704) = 0.2176 * 1.1296 = 0.24580096

    Repeat the formula to further improve the guess.

    Write a function that takes a given ``A`` and ``B`` and then writes out ``A/B``
    without using a single division.
    
    You will need to create a additional function ``newtons1overX(b)`` that takes a
    single parameter ``b`` and returns its reciprocal. You will need to think of an
    appropriate ending condition for the loop that calculates ``1/B``.

    Unfortunately, the first guess for this function should be between zero and the true
    value of ``1/B``. It sounds like this might call for division, but this can be avoided
    by starting with a very tiny first guess of ``1.0E-14``. Make the first guess negative if ``B``
    is negative, and positive if ``B`` is positive. For some large values of ``B``,
    your first guess might not be tiny enough, so protect your code with an
    if statement that determines when B is too large. Also, the reciprocal of
    zero is not defined, so use an if statement to test for this, and return the
    Python value ``None``.

    ~~~~

    # My Name:

    def newtons1overX(b):
        # Write your code here
    
    def main():
        a = 355
        b = 113
        oneOverX = newtons1overX(b)
        if oneOverX == None:
            print("reciprocal of zero is not defined")
        else:
            print(str(a) + "/" + str(b) + " = " + str(a * oneOverX))

    if __name__ == "__main__":
        main()
        
    ==== 
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
    
        def _newtons1overX(self, b):
            x = 1.0E-300

            if b == 0:
                x = None
            else:
                if b < 0:
                    x = -x
                while abs( b * x - 1 ) > 1.0E-14:
                    x = x * ( 2 - b * x )

            return x
    
        def testOne(self):
            print("Begin Auto-Test")
            b = 113
            self.assertAlmostEqual(newtons1overX(b), self._newtons1overX(b), 5, "checking b = " + str(b))
            b = -64
            self.assertAlmostEqual(newtons1overX(-b), self._newtons1overX(-b), 5, "checking b = " + str(b))
            b = 0
            self.assertEqual(newtons1overX(0), self._newtons1overX(0), "checking b = " + str(b))
            
    myTests().main()