.. actex:: ch_cl2_q6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: ClassesDiggingDeeper
   :subchapter: Exercises
   :topics: ClassesDiggingDeeper/Exercises
   :from_source: T
   :nocodelens:

   Write a new method in the Rectangle class to test if a Point falls within
   the rectangle.  For this exercise, assume that a rectangle at (0,0) with
   width 10 and height 5 has *open* upper bounds on the width and height,
   i.e. it stretches in the x direction from [0 to 10), where 0 is included
   but 10 is excluded, and from [0 to 5) in the y direction.  So
   it does not contain the point (10, 2).  These tests should pass::

      r = Rectangle(Point(0, 0), 10, 5)
      test(r.contains(Point(0, 0)), True)
      test(r.contains(Point(3, 3)), True)
      test(r.contains(Point(3, 7)), False)
      test(r.contains(Point(3, 5)), False)
      test(r.contains(Point(3, 4.99999)), True)
      test(r.contains(Point(-3, -3)), False)
   ~~~~