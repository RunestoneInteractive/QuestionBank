.. activecode:: CSC101-temperature-program
    :author: Isaac Sung
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens:

    Modify the following program so that it will convert degrees fahrenheit to degrees celsius (change the ``deg_f`` assignment in ``c_to_f``).
    ~~~~
    deg_c = int(input("What is the temperature in Celsius? "))

    # formula to convert C to F is: (degrees Celsius) times (9.0/5.0) plus (32)
    deg_f = 0 # ---Fix this---

    print(deg_c, " degrees Celsius is", deg_f, " degrees Farenheit.")

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            print( c_to_f( 37 ) )
            self.assertAlmostEqual (  c_to_f( 37 ), 98.6, 2,"Testing that c_to_f(37) = 98.6") 
 
    myTests().main()