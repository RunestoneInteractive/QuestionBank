.. codelens:: clens11_8_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Functions
    :subchapter: GlobalVariables
    :topics: Functions/GlobalVariables
    :from_source: T
    :python: py3

    def square(x):
        y = x * x
        x = 0       # assign a new value to the parameter x
        return y

    x = 2
    z = square(x)
    print(z)