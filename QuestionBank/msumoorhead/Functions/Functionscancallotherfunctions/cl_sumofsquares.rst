.. codelens:: cl_sumofsquares
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: Functionscancallotherfunctions
    :topics: Functions/Functionscancallotherfunctions
    :from_source: None

    def square(x):
        y = x * x
        return y

    def sum_of_squares(x, y, z):
        a = square(x)
        b = square(y)
        c = square(z)

        return a + b + c

    a = -5
    b = 2
    c = 10
    result = sum_of_squares(a, b, c)
    print(result)