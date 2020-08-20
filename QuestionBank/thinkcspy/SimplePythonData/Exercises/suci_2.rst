.. activecode:: suci_2
    :author: peter suci
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens:

    Write a program that adds two numbers.
    ~~~~
    sum = 4 + 5
    print("sum", sum)



    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            print( c_to_f( 37 ) )
            self.assertAlmostEqual (  c_to_f( 37 ), 98.6, 2,"Testing that c_to_f(37) = 98.6") 
 
    myTests().main()