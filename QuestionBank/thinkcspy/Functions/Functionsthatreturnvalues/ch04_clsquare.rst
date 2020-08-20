.. codelens:: ch04_clsquare
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Functionsthatreturnvalues
    :topics: Functions/Functionsthatreturnvalues
    :from_source: T

    def square(x):
        y = x * x
        return y

    toSquare = 10
    squareResult = square(toSquare)
    print("The result of", toSquare, "squared is", squareResult)