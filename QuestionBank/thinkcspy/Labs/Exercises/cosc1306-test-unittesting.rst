.. activecode:: cosc1306-test-unittesting
    :author: Mohammad Rajiur Rahman
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest

    #If this is a homework problem instead of an example in the text
    #then the assignment text should go here.  The assignment text ends with
    #the line containing four tilde 
    
    # ~~~~~
    
    def add(N):
        sum = 0
        for n in range(N+1):
            sum = sum + n
        return sum 
   
    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):

            self.assertEqual(add(2),2,"A feedback string when the test fails")
            self.assertEqual(add(10),55,"A feedback string when the test fails")
            #self.assertAlmostEqual(add(10), 55, 1, "Try adding your parmeters")


    myTests().main()