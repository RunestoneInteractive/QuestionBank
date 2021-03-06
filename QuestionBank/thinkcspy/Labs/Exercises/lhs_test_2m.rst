.. activecode:: lhs_test_2m
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5
    :total_students_attempting: 10
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 1.0

    **(10 pts)** Write a function called ``printMsg(message, howMany)`` that prints out the string ``message``
    as many times as the input ``howMany`` specifies.
    
    So, for example, ``printMsg("This is easy!", 3)`` will print:
    
    ::
    
      This is easy!
      This is easy!
      This is easy!
    
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    '''
    def printMsg(message, n):
        for i in range(n):
            print(message)
    '''
    import sys
    from unittest.gui import TestCaseGui
            
    class myTests(TestCaseGui):
    
        def golden_printMsg(self, message, n):
            golden_out = ''
            for i in range(n):
                golden_out = golden_out + message + '\n'
            return golden_out
                 
        def check(self, message, n):
    
            # run test and steer print() to output file
            fname = "test.out"
            sys.stdout = open(fname, "w")
            printMsg(message, n)
            sys.stdout.close()
    
            # get output
            f = open(fname, "f")
            outText = f.read()
            f.close()
    
            self.assertEqual(outText, self.golden_printMsg(message, n), "Test")
    
            self.deleteFile(fname)
    
        def testOne(self):
    
            self.check("Hello", 5)
            self.check("This is a test", 1)
            self.check("This is another test", 10)
            self.check("This is yet another test", 0)
              
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print("", end="")
            sys.stdout.close()
    
    myTests().main()