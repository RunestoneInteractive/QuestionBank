.. activecode:: fnh
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: Functionsthatreturnvalues
    :topics: Functions/Functionsthatreturnvalues
    :from_source: None

    def square(x):

        y = x * x
        return y

    toSquare = 10
    result = square(toSquare)
    print("The result of ", toSquare, " squared is ", result)