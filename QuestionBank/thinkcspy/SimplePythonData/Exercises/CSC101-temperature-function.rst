.. activecode:: CSC101-temperature-function
    :author: Yan Chen
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.1666666667
    :total_students_attempting: 6
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.5

    Modify the following program so that it will convert degrees fahrenheit to degrees celsius (change the ``deg_f`` assignment in ``c_to_f``).
    ~~~~
    def c_to_f (deg_c):
        # formula to convert C to F is: (degrees Celsius) times (9.0/5.0) plus (32)
        deg_f = 0 # ---Fix this---
        return deg_f
    
    deg_c = int(input("What is the temperature in Celsius? "))
    
    print(deg_c, " degrees Celsius is", c_to_f( deg_c ), " degrees Farenheit.")
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            print( c_to_f( 37 ) )
            self.assertAlmostEqual (  c_to_f( 37 ), 98.6, 2,"Testing that c_to_f(37) = 98.6") 
    
    myTests().main()