.. activecode:: q7_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: T
    :nocodelens:

    from test import testEqual

    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

    testEqual(is_even(10), True)
    testEqual(is_even(5), False)
    testEqual(is_even(1), False)
    testEqual(is_even(0), True)