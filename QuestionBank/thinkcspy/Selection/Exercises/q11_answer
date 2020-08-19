.. activecode:: q11_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: T
    :nocodelens:

    from test import testEqual

    def is_rightangled(a, b, c):
        is_rightangled = False

        if a > b and a > c:
            is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
        elif b > a and b > c:
            is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
        else:
            is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
        return is_rightangled

    testEqual(is_rightangled(1.5, 2.0, 2.5), True)
    testEqual(is_rightangled(4.0, 8.0, 16.0), False)
    testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
    testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
    testEqual(is_rightangled(4.1, 8.2, 9.168), False)
    testEqual(is_rightangled(0.5, 0.4, 0.64031), True)