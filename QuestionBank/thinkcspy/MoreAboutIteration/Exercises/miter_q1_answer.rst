.. activecode:: miter_q1_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: T

    def newtonSqrt(n):
        approx = 0.5 * n
        better = 0.5 * (approx + n/approx)
        while better != approx:
            approx = better
            better = 0.5 * (approx + n/approx)
            print("Approx:", better)
        return approx


    print("Final approx:", newtonSqrt(25))