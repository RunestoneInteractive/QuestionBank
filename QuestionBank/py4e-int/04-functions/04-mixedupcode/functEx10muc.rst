.. parsonsprob:: functEx10muc
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-mixedupcode
    :topics: 04-functions/04-mixedupcode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    The following code creates three functions that calculate geometric equations. First create a function
    called distance, which finds and returns the distance between two coordinates, using the distance formula
    where d = √((x_2-x_1)²+(y_2-y_1)²). Then, create a function called area, which returns the area of a
    circle given the radius, using the formula A = πr². Finally, create a function called area2, which uses
    the previous two functions to return the area of a given circle. Remember that ** is exponent notation
    in Python and watch your indentation!
    -----
    def distance(x1, y1, x2, y2):
    =====
        dx = x2 - x1
        dy = y2 - y1
    =====
        dsquared = dx**2 + dy**2
    =====
        result = dsquared**0.5
    =====
        return result
    =====
    def area(radius):
    =====
        b = 3.14159 * radius**2
    =====
        return b
    =====
    def area2(xc, yc, xp, yp):
    =====
        radius = distance(xc, yc, xp, yp)
    =====
        result2 = area(radius)
    =====
        return result2