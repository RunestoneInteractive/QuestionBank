.. activecode:: sks_hw2_ex5
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    
    One of the more amazing facts from calculus is that the following sum gets closer and 
    closer to the value ``e^x`` the more terms you add in: ::

        e^x = 1 + x + x^2/2! +  x^3/3! +  x^4/4! + x^5/5! +  x^6/6! + . . . .
        
    Remember that ``n!`` means n factorial, ``n*(n-1)*(n-2)* ... *1``. For example,
    if ``x`` is ``2`` then ::

        e^2 = 1 + 2 + 2^2/2! + 2^3/3! + 2^4/4! + 2^5/5!  . . . .
        e^2 = 1 + 2 + 4/2 + 8/6 + 16/24 + 32/120 + . . . .

        e^2 = 1 + 2 +  2  + 1.3333 + 0.6666 + 0.2666 + . . . .

        e^2 ~ 7.266


    More exactly, ``e^2 = 7.38907...``

    Write a function that takes the power ``x`` as a parameter, then calculates ``e^x`` using
    a ``while`` loop to add up successive terms until the current term is less than
    ``1.0E-12``. The function should then return the calculated value of ``e^x``.
    
    Lastly, you should write out your value and the value of ``math.exp(x)`` to see how your value compares.

    To do this program sensibly, the loop will add in a ``term`` each iteration. ::

        sum = sum + term;

    Look carefully at the first equation for ``e^x``. Notice that each ``term`` is: ::

        x^N/N! 
    
    for some N. This is the same as: ::

        x^(N-1)/(N-1)! *  x/N

    This is the same as the previous ``term`` times ``x/N``. So each iteration of the loop merely
    has to multiply the previous ``term`` by ``x/N`` and add it to the accumulating sum. Note
    that you DO NOT USE ``math.factorial()``.

    Don't let the math scare you away! This is actually a fairly easy program, and is
    typical of a type of calculation that computers are often used for. ::

        n: 1    term: 2.0   sum: 3.0
        n: 2    term: 2.0   sum: 5.0
        n: 3    term: 1.33333333333     sum: 6.33333333333
        n: 4    term: 0.666666666667    sum: 7.0
        n: 5    term: 0.266666666667    sum: 7.26666666667
        n: 6    term: 0.0888888888889   sum: 7.35555555556
        n: 7    term: 0.0253968253968   sum: 7.38095238095
        n: 8    term: 0.00634920634921  sum: 7.3873015873
        n: 9    term: 0.00141093474427  sum: 7.38871252205
        n: 10   term: 0.000282186948854     sum: 7.38899470899
        n: 11   term: 5.13067179734e-05     sum: 7.38904601571
        n: 12   term: 8.55111966223e-06     sum: 7.38905456683
        n: 13   term: 1.31555687111e-06     sum: 7.38905588239
        n: 14   term: 1.87936695873e-07     sum: 7.38905607033
        n: 15   term: 2.50582261164e-08     sum: 7.38905609538
        n: 16   term: 3.13227826455e-09     sum: 7.38905609852
        n: 17   term: 3.68503325242e-10     sum: 7.38905609888
        n: 18   term: 4.09448139157e-11     sum: 7.38905609893
        n: 19   term: 4.30998041218e-12     sum: 7.38905609893
        n: 20   term: 4.30998041218e-13     sum: 7.38905609893
        my e^x: 7.38905609893
        real e^x: 7.38905609893

    **HINT**: You will need two tabs on each line to format it cleaner and match accurately.

    ~~~~

    # My Name:
    
    # don't forget to import the math library...

    def eToX(x):
        # Write your code here
    
    def main():
        # write your code here

    if __name__ == "__main__":
        main()
        
    ==== 
    import re
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
    
        def _eToX(self, x):
            term = 1.0
            sum = 1.0
            n = 1;
            outStr = ""

            while term > 1.0E-12:
                term = term * x / n
                sum = sum + term
                outStr += "n: " + str(n) + " \tterm: " + str(term) + " \tsum: " + str(sum) + "\n"
                n = n + 1
            outStr += "my e^x: " + str(sum) + "\n"
            outStr += "real e^x: " + str(math.exp(x)) + "\n"
            return sum, outStr
    
        def testOne(self):
            print("Begin Auto-Test")
            editText = self.getEditorText()
            self.assertEqual(0, len(re.findall("\s*factorial[( ]", editText)), "Should be no 'factorial'")
            self.assertEqual(1, len(re.findall("\s*while[( ]", editText)), "Should use 1 'while'")
            x = 1.5
            eToXexpected, expected = self._eToX(x)
            #print(expected)
            oLen = len(self.getOutput())
            eToXactual = eToX(x)
            oLenTest = len(self.getOutput())
            actual = self.getOutput()[oLen:oLenTest]  #extract new output

            actual = " ".join(actual.split())
            expected = " ".join(expected.split())

            self.assertEqual(actual, expected, "checking output for eToX(" + str(x) + ")")
            
    myTests().main()