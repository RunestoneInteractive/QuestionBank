.. codelens::  clens11_8_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Functions
    :subchapter: GlobalVariables
    :topics: Functions/GlobalVariables
    :from_source: T
    :python: py3

    def powerof(x,p):
        global power  # a really...
        power = p     # ...bad idea, but valid code
        y = x ** power
        return y

    power = 3
    result = powerof(10,2)
    print(result)
    print(power)