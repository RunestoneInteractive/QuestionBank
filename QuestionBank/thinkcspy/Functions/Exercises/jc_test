.. activecode:: jc_test
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Write a non-fruitful function ``skipForward(t, len)`` that moves turtle t forward len units without drawing anything
  

    ~~~~

    def skipForward(t,len):
        """ Moves the turtle t forward len units without drawing anything. """
        # Put your code here

    ====
    import turtle
    import math
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            wn = turtle.Screen() 
            t = turtle.Turtle()
            wn.setup(width=2,height=2)
            t.goto(100,100)
            skipForward(t,10)
            self.assertAlmostEqual(t.xcor(),110.0,0,"Tested skipForward(10) starting at 100")
            t.goto(20,20)
            t.left(90)
            skipForward(t, -30)
            self.assertAlmostEqual(t.ycor(),-10.0,0,"Tested skipForward(-30) starting at 20")
            t.goto(20,20)
            t.left(90)
            skipForward(t, 0)
            self.assertAlmostEqual(t.ycor(),20.0,0,"Tested skipForward(0) starting at 20")
            t.reset()
            t.left(45)
            skipForward(t, 5)
            self.assertAlmostEqual(t.xcor(),math.sqrt(25/2),0,"Tested skipForward(5) starting at 0, 45 degree angle")


    myTests().main()