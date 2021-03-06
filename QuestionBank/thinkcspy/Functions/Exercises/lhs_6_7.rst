.. activecode:: lhs_6_7
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.3652849741
    :total_students_attempting: 386
    :num_students_correct: 370.0
    :mean_clicks_to_correct: 6.1864864865

    Write a function ``addUpSquaresAndCubes`` that adds up the squares and adds up the cubes of integers from 1 to N, where N is entered by the user. 
    This function should return two values - the sum of the squares and the sum of the cubes.
    Use  just **one loop** that generates the integers and accumulates the sum of squares and the sum of cubes. 
    
    Then, write two separate functions ``sumOfSquares`` and ``sumOfCubes`` to calculate the sums of the squares and sum of the cubes using the explicit formula below.
    
    ::
    
            1**2 + 2**2 + 3**2 + ... + n**2 = n(n+1)(2n+1)/6
            1**3 + 2**3 + 3**3 + ... + n**3 = n**2(n+1)**2/4
    
    Write functions to add these formulas to your program and print out their results as well as that of the explicit summations. The user dialog will look something like this:
    
    **Warning:** The equations above a **math** equation and the syntax may not work for python as written.
    ::
    
            The sum of Squares is  55
            The sum of Cubes   is  225
    
            The explicit sum of Squares is  55
            The explicit sum of Cubes   is  225
    
    ~~~~
    # My Name:
    
    def addUpSquaresAndCubes( n ):
        # write your code here
        # calculate using one for loop with accumulator
        sumOfSquares = ...
        sumOfCubes = ...
    
        return(sumOfSquares, sumOfCubes)  # return two values for this function
    
    def sumOfSquares( n ):
        # write your code here
        # calculate using the explicit formulas - n(n+1)(2n+1)/6
    
    def sumOfCubes( n ):
        # write your code here
        # calculate using the explicit formulas - n^2(n+1)^2/4
    
    def main():
        squares, cubes = addUpSquaresAndCubes(N)
        print("The sum of Squares is", squares)
        print("The sum of Cubes   is", cubes)
        print("The explicit sum of Squares is", sumOfSquares(N))
        print("The explicit sum of Cubes   is", sumOfCubes(N))
    
    if __name__ == "__main__":
        main()
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
           
        def _golden(self, n):
            a = n*(n+1)*(2*n+1)/6
            b = n**2*(n+1)**2/4
            return ( (a,b), a, b )
    
         # regExString - is checked inside inString
         # howMany - how many matches are expected
         # matchString - summary of what is being matched (readable version of regExString)
         # errorString - error string upon assertion failure
        def regExCheck(self, regExString, inString, howMany, matchString, errorString):
            res = re.findall(regExString, inString, re.M)
            checkOK = (len(res) == howMany)
            if not checkOK:
                print("Found [", matchString, "]", len(res), "time(s), not", howMany)
    
            self.assertEqual(checkOK, True, errorString)
    
            return(checkOK)
    
        def testOne(self):
            print("Auto-testing...")
            outText = self.getOutput()
            code = self.getEditorText()
            
            # strips this test code - when testing code with this test code 
            pos = code.find("class myTests")
            if (pos != -1):
                code = code[:pos]
    
            regEx = "(?:^def\s+addUpSquaresAndCube.*\n)(?:.*\n)*(^\s+for\s+\w+\s+in.*:.*\n)(?:.*\n)*(?:^\s+return)"
    
            if not self.regExCheck(regEx, code, 1, "'for' loop in addUpSquaresAndCubes()", "Should be using a for loop"):
                return
    
            testcases = [7, 9, 1, 0]
            for n in testcases:
                answer = (addUpSquaresAndCubes(n), sumOfSquares(n), sumOfCubes(n))
                correct = self._golden(n)
                self.assertEqual(answer, correct, "testing all 3 functions w/ n = " + str(n))
    
    myTests().main()