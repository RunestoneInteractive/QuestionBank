.. activecode:: func_q15_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: T

    def myPi(iters):
        ''' Calculate an approximation of PI using the Leibniz
        approximation with iters number of iterations '''
        pi = 0
        sign = 1
        denominator = 1
        for i in range(iters):
            pi = pi + (sign/denominator)
            sign = sign * -1  # alternate positive and negative
            denominator = denominator + 2

        pi = pi * 4.0
        return pi

    pi_approx = myPi(10000)
    print(pi_approx)