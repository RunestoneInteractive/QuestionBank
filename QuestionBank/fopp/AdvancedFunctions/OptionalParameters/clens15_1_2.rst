.. codelens:: clens15_1_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: AdvancedFunctions
    :subchapter: OptionalParameters
    :topics: AdvancedFunctions/OptionalParameters
    :from_source: T
    :python: py3

    initial = 7
    def f(x, y =3, z=initial):
        print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

    initial = 10
    f(2)