.. activecode:: LHSChapterFifteenQuestionFive
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
    :mean_clicks_to_correct: 33.0

    Pascal’s triangle is a number triangle with numbers arranged in
    staggered rows such that
    
                a\ :sub:`nr` = n! / r!(n - r)!
    
    This equation is the equation for a binomial coefficient. You can
    build Pascal’s triangle by adding the two numbers that are diagonally
    above a number in the triangle. An example of Pascal’s triangle is
    shown below.
    
    ::
    
                          1
                        1   1
                      1   2   1
                    1   3   3   1
                  1   4   6   4   1
    
    Write a program that prints out Pascal’s triangle. Your program
    should accept a parameter that tells how many rows of the triangle to
    print.
    
    ~~~~
    def pascal(n, k):
        # Your recursive code here
    
    def print_triangle(rows):
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
                return 1
            else:
                return int(self._pascal(n - 1, k - 1)) + int(self._pascal(n - 1, k))
    
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
            print('Auto-testing...')
            editText = self.getEditorText()
            start = editText.find("def pascal")
            end = editText.find("def print_triangle")
            pascalCode = editText[start:end]
            #print(pascalCode)
            self.assertEqual(0, len(re.findall("\s*while[( ]", pascalCode)), "Should use no 'while' loops")
            self.assertEqual(0, len(re.findall("\s*for ", pascalCode)), "Should use no 'for' loops")
            
            oLen = len(self.getOutput())
            print_triangle(6)
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #remove original output from test string
            s = "".join(outText.split())
            self.assertIn("11112113311464115101051", s, "checking console output")
    
            for row in range(4):
                for col in range(row + 1):
                    self.assertEqual( self._pascal(row, col), pascal(row, col), "Testing pascal("+str(row)+", "+str(col)+")")
    myTests().main()