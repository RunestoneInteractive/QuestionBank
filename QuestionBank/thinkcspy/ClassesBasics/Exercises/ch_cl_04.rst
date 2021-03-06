.. actex:: ch_cl_04
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: ClassesBasics
   :subchapter: Exercises
   :topics: ClassesBasics/Exercises
   :from_source: T
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   The equation of a straight line is  "y = ax + b", (or perhaps "y = mx + c").
   The coefficients a and b completely describe the line.  Write a method in the
   Point class so that if a point instance is given another point, it will compute the equation
   of the straight line joining the two points.  It must return the two coefficients as a tuple
   of two values.  For example,   ::
   
      >>> print(Point(4, 11).get_line_to(Point(6, 15)))
      >>> (2, 3)
   
   This tells us that the equation of the line joining the two points is "y = 2x + 3".
   When will your method fail?
   ~~~~