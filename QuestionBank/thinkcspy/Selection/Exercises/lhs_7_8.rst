.. activecode:: lhs_7_8
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0707317073
    :total_students_attempting: 410
    :num_students_correct: 367.0
    :mean_clicks_to_correct: 18.3514986376

    Write a function ``printNice(a, b)`` that takes two integer inputs. 
    
    ``a`` and ``b`` are the coefficients of
    the equation ``ax + b``. The function will print out a "nice" simplified expression.
    
    Example: a = 5 and b = 2  ==> ``5x + 2``
    
    Example: a = 2 and b = 0  ==> ``2x``
    
    Example: a = 1 and b = -6  ==> ``x - 6``
    
    Other example outputs are below:
    
    ::
    
      2x - 7
      -14x
      17
      -x + 9
      -8
      0
    
    **REMEMBER:** You can use ``print('x', end='')`` so that just an ``x`` is printed with no space or newline
    at the end.
    
    ~~~~
    # Name: 
    
    def printNice(a, b):
        # write your code here
    
    def main():
        printNice(2, -7)	# sample test code - you can make your own...
        printNice(-1, 9)
        printNice(-14, 0)
        
    main()
    
    ====
    import random
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def golden_test(self, a, b):
            out = ""
            if a != 0:
                if a == 1:
                    out = "x"
                elif a == -1:
                    out = "-x"
                else:
                    out = str(a) + "x"
                if b >= 1:
                    out = out + " + " + str(b)
                elif b < 0:
                    out = out + " - " + str(-b)
                out = out + "\n"
            else:
                out = str(b) + "\n"
            return(out)
    
        def runOne(self, a, b):
            oLen = len(self.getOutput())
            printNice(a, b)
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #extract new output           
            self.assertEqual( outText, self.golden_test(a, b), "Check")    
            
        def testOne(self):
            print("Begin Auto-Test")
            self.runOne(5, 2)
            self.runOne(6, 0)
            self.runOne(7, -1)
            self.runOne(1, 11)
            self.runOne(1, 0)
            self.runOne(1, -4)
            self.runOne(-1, 6)
            self.runOne(0, 3)
            self.runOne(0, -1)
            self.runOne(0, 0) 
            self.runOne(random.randrange(-3, 3), random.randrange(-3, 3))
            
    myTests().main()