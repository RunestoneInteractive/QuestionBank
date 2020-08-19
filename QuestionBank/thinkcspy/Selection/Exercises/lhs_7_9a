.. activecode:: lhs_7_9a
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4864197531
    :total_students_attempting: 405
    :num_students_correct: 403.0
    :mean_clicks_to_correct: 3.0148883375

    Write a function ``printWinner(winner)`` that takes the integer winner and prints out a message
    according to who won.
    
    1:  "I won!"
    
    0:  "Tie..."
    
    -1: "You won!"
    
    anything besides 1, 0 or -1: "Unknown winner value for this function"
    
    ~~~~
    # Name:
    
    # define function here
        '''print out a message of who wins depending on the value of the integer winner:
               1  : "I won!"
               -1 : "You won!"
               0  : "Tie..."
               none of these: "Unknown winner value for this function"
        '''
        # write code here
        
    # define main here
        # call it and test it out here...
        
    if __name__ == "__main__":
        main()
        
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def golden_Winner(self, winner):
            if winner == 1:
                out = "I won!\n"
            elif winner == -1:
                out = "You won!\n"
            elif winner == 0:
                out = "Tie...\n"
            else:
                out = "Unknown winner value for this function\n"
            return(out)
        
        def checkFuncOutput(self, winner):
            oLen = len(self.getOutput())
            printWinner(winner)
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #extract new output           
            self.assertEqual(outText, self.golden_Winner(winner), "Check winner")  
                
        def testOne(self):
            print("Auto-testing...")
            self.checkFuncOutput(-1)
            self.checkFuncOutput(1)
            self.checkFuncOutput(0) 
            self.checkFuncOutput(10)
            
    myTests().main()