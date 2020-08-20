.. parsonsprob:: functEx3muc
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

    Create two functions. The first is called square, which returns a number squared. The second is called
    sum_of_squares, which returns the sum of the squares of three numbers. Watch your indentation.
    -----
    def square(x):
    =====
        y = x * x
    =====
        return y
    =====
    def sum_of_squares(x, y, z):
    =====
        a = square(x)
        b = square(y)
              c = square(z)
    =====
        return a + b + c