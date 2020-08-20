.. activecode:: lhs_17_2a
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0925
    :total_students_attempting: 400
    :num_students_correct: 385.0
    :mean_clicks_to_correct: 10.587012987

    Write two methods that change the state of a ``Rectangle`` by making an assignment
    to its ``width``, ``height`` or ``location`` attributes. Write a ``grow`` method that will
    increase (or decrease) the size of this ``Rectangle`` and a ``move`` method that will
    change this objects location.
    
    The ``grow`` and ``move`` methods output should be as follows:
    
        >>> r = Rectangle(Point(10,5), 100, 50)
        >>> print(r)
        ((10, 5), 100, 50)
        >>> r.grow(25, -10)
        >>> print(r)
        ((10, 5), 125, 40)
        >>> r.move(-10, 10)
        print(r)
        ((0, 15), 125, 40)
        
    ~~~~
    import test, math
    
    class Point:
        """ Point class for representing and manipulating x,y coordinates. """
    
        # Use your rectangle class from previous exercises
    
    
    class Rectangle:
        """Rectangle class using Point, width and height"""
    
        # Use your rectangle class from previous exercises
    
        def grow(self, delta_width, delta_height):
            """ Grow (or shrink) this object by the deltas """
            # define grow method for the rectangle
            
        def move(self, dx, dy):
            """ Move this object by the deltas """
            # define move method for the rectangle
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
        def testOne(self):
    
            r = Rectangle(Point(10, 5), 100, 50)
            r.grow(25, -10)
            self.assertEqual(r.getWidth(), 125, 'testing getWidth() after grow()' )
            self.assertEqual(r.getHeight(), 40, 'testing getHeight() after grow()' )
            r.move(-10, 10)
            self.assertEqual(r.location.getX(), 0, 'testing location.getX() after move()' )
            self.assertEqual(r.location.getY(), 15, 'testing location.getY() after move()' )
    
            r = Rectangle(Point(10, 5), 100, 50)
            r.grow(-25, 10)
            self.assertEqual(r.getWidth(), 75, 'testing getWidth() after grow()' )
            self.assertEqual(r.getHeight(), 60, 'testing getHeight() after grow()' )
            r.move(10, -10)
            self.assertEqual(r.location.getX(), 20, 'testing location.getX() after move()' )
            self.assertEqual(r.location.getY(), -5, 'testing location.getY() after move()' )
        
    myTests().main()