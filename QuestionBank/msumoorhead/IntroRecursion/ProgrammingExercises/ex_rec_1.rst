.. actex:: ex_rec_1
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: IntroRecursion
    :subchapter: ProgrammingExercises
    :topics: IntroRecursion/ProgrammingExercises
    :from_source: None

    def computeFactorial(number):
        #your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(computeFactorial(0),1,"Tested computeFactorial on input 0")
            self.assertEqual(computeFactorial(1),1,"Tested computeFactorail on input 1")
            self.assertEqual(computeFactorial(2),2,"Tested computeFactorial on input 2")
            self.assertEqual(computeFactorial(3),6,"Tested computeFactorial on input 3")
            self.assertEqual(computeFactorial(4),24,"Tested computeFactorial on input 4")
            self.assertEqual(computeFactorial(8),40320,"Tested computeFactorial on input 8")
            self.assertEqual(computeFactorial(-5),None,"Tested computeFactorial on a negative number - make sure to handle this case")

    myTests().main()