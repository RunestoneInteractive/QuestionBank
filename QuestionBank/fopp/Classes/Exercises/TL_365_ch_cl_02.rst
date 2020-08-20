.. actex:: TL_365_ch_cl_02
   :author: Tyler Luchko
   :difficulty: 1.2234224253
   :basecourse: fopp
   :chapter: Classes
   :subchapter: Exercises
   :topics: Classes/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2448979592
   :total_students_attempting: 49
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 4.7931034483

   Add a method called ``move`` that will take two parameters, call
   them ``dx`` and ``dy``.  The method will cause the point to move in
   the x and y direction the number of units given. (Hint: you will
   change the values of the state of the point)
   
   ~~~~
   
   class Point:
       """ Point class for representing and manipulating x,y coordinates. """
   
       def __init__(self, initX, initY):
   
           self.x = initX
           self.y = initY
   
       def getX(self):
           return self.x
   
       def getY(self):
           return self.y
   
       def distanceFromOrigin(self):
           return ((self.x ** 2) + (self.y ** 2)) ** 0.5
   
       # Put your new method here
     
       def __str__(self):
           return str(self.x)+","+str(self.y)
   ====
   
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           class _Point:
        """ Point class for representing and manipulating x,y coordinates. """
   
        def __init__(self, initX, initY):
   
            self.x = initX
     self.y = initY
   
               def getX(self):
                   return self.x
   
               def getY(self):
                   return self.y
   
               def distanceFromOrigin(self):
                   return ((self.x ** 2) + (self.y ** 2)) ** 0.5
   
               def move(self, dx, dy):
                   self.x += dx
            self.y += dy
     
               def __str__(self):
                   return str(self.x)+","+str(self.y)
   
   
    def test_point(pt, dx, dy):
        point = Point(pt[0], pt[1])
        _point= _Point(pt[0], pt[1])
        point.move(dx, dy)
        _point.move(dx, dy)
        self.assertAlmostEqual(point.x, _point.x, 7,
            'Checking x for Point({}, {}).move({}, {})'.format(pt[0], pt[1], dx, dy))
        self.assertAlmostEqual(point.y, _point.y, 7,
            'Checking y for Point({}, {}).move({}, {})'.format(pt[0], pt[1], dx, dy))
    test_point([0.29, 0.87], 0.8, 0.2)
    test_point([0.13, 0.95], 0.89, 0.32)
   myTests().main()