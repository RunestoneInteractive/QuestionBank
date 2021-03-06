.. activecode:: LHSChapterFifteenQuestionSeven
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
    :mean_clicks_to_correct: 4.0

    Consider this definition of the sum of the elements in an integer list:
    
    .. sourcecode:: python
    
        sum( intList ) = sum( intList, 0 )
    
        sum( intList, index ) = 0, if index == len(intList)
    
        sum( intList, index ) = intList[index] + sum( intList, index+1), if index < len(intList)
    
    Write a recursive Python function that implements this definition and a program to test it.
    ~~~~
    def sum(intList, index = 0):
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
    
            self.assertEqual(0, sum([]), "Testing sum([])")
            self.assertEqual(10, sum([1, 2, 3, 4]), "Testing sum([1, 2, 3, 4])")
            self.assertEqual(8769, sum([17, 123, 87, 34, 66, 8398, 44]), "Testing sum,([17, 123, 87, 34, 66, 8398, 44])")
            self.assertEqual(5, sum([12, 123, 4, 1], 2), "Testing sum([12, 123, 4, 1], 2)")
            self.assertEqual(0, sum([12, 123, 4, 1], 7), "Testing sum([12, 123, 4, 1], 7)")
    myTests().main()