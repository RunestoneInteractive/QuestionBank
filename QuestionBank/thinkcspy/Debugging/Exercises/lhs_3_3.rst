.. activecode:: lhs_3_3
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Debugging
    :subchapter: Exercises
    :topics: Debugging/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.0851788756
    :total_students_attempting: 587
    :num_students_correct: 518.0
    :mean_clicks_to_correct: 4.7027027027

    The harmonic mean of two numbers is given by: ``H = 2 / ( 1/X + 1/Y )``. This is sometimes more useful than the more usual average of two numbers. The following program inputs two numbers (as floating point) and writes out both the usual average (the arithmetic mean) and the harmonic mean. The program, however does not work. Find and fix the error(s):
    
    ~~~~
    x = input("Enter X:")
    y = input("Enter Y:"]
    
    x = int(x)
    y = int(y)
    
    aritmeticMean = ( x + y ) // 2
    print("Arithmetic mean: ", aritmeticMean)
    
    harmonicMean = 2 / ( 1 / x + 1 / y )
    println(""Harmonic   mean: """, harmonicMean)
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            aMean = (float(x) + float(y)) / 2
            hMean = 2 / ( 1 / float(x) + 1 / float(y) )
            outText = " ".join(self.getOutput().split()) # remove extra spaces in the output
            self.assertIn('Arithmetic mean: ' + str(aMean), outText, "Actual is correct output. Expected is your program output.")
            self.assertIn('Harmonic mean: ' + str(hMean), outText, "Actual is correct output. Expected is your program output.")
    
    myTests().main()