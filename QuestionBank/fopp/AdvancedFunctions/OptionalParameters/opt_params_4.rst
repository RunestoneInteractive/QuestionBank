.. codelens:: opt_params_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: AdvancedFunctions
    :subchapter: OptionalParameters
    :topics: AdvancedFunctions/OptionalParameters
    :from_source: T
    :python: py3

    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))
    print(f(4, ["Hello"]))
    print(f(5, ["Hello"]))