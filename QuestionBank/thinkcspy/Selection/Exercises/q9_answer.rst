.. activecode:: q9_answer
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

    def is_odd(n):
        if is_even(n):
            return False
        else:
            return True

    testEqual(is_odd(10), False)
    testEqual(is_odd(5), True)
    testEqual(is_odd(1), True)
    testEqual(is_odd(0), False)