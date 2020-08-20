.. activecode:: lhs_7_7
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1262886598
    :total_students_attempting: 388
    :num_students_correct: 375.0
    :mean_clicks_to_correct: 11.016

    Write a function ``printHeight`` that takes in a integer input that describes the height in inches.
    The function is a non-fruitful function that prints out a statement converting the inches into feet and inches.
    Be careful for certain special grammatical cases.  
    
    ``printHeight(48)`` should print out ``4 feet``.
    
    ``printHeight(55)`` should print out ``4 feet and 7 inches``
    
    ``printHeight(49)`` should print out ``4 feet and 1 inch``
    
    See other grammar examples.
    
    ::
    
      7 feet and 2 inches
      9 feet
      1 foot and 9 inches
      1 foot
      3 inches
      1 inch
      0 inches
    
    ~~~~
    # Name: 
    
    def printHeight(inches):
        # write your code here
    
    def main():
        printHeight(72)
        printHeight(80)
        printHeight( tryOtherNumbers )
        
    if __name__ == "__main__":
        main()
    
    ====
    import re
    import random
    from unittest.gui import TestCaseGui
        
    class myTests(TestCaseGui):
             
        def golden_test(self, inches):
            feet = inches // 12
            inch = inches % 12
            out = ""
            if feet != 0:
                out = out + str(feet)
                if feet == 1:
                    out = out + " foot"
                else:
                    out = out + " feet"
                if inch != 0:
                    if inch == 1:
                        out = out + " and 1 inch\n"
                    else:
                        out = out + " and " + str(inch) + " inches\n"
                else:
                    out = out + "\n"
            else:
                if inch == 0:
                    out = "0 inches\n"
                elif inch == 1:
                    out = "1 inch\n"
                else:
                    out = str(inch) + " inches\n"
            return(out)
                
        def check(self, h):
            oLen = len(self.getOutput())
            printHeight(h)
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #extract new output           
            self.assertEqual( outText, self.golden_test(h), "Check " + str(h))   
    
        def testOne(self):
            print("Auto-testing...")
    
            testList = [62, 60, 14, 13, 12, 5, 1, 0]
            for h in testList:
                self.check(h)
    
            for i in range(2):
                rand = random.randrange(0,30,1)
                self.check(rand)
    
    myTests().main()