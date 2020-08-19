.. activecode:: ch06_newarea
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Composition
    :topics: Functions/Composition
    :from_source: T

    def distance(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            dsquared = dx**2 + dy**2
            result = dsquared**0.5
            return result

    def area(radius):
        b = 3.14159 * radius**2
        return b

    def area2(xc, yc, xp, yp):
        radius = distance(xc, yc, xp, yp)
        result = area(radius)
        return result

    print(area2(0,0,1,1))