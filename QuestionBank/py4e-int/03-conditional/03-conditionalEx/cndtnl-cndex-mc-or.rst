.. mchoice:: cndtnl-cndex-mc-or
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-conditionalEx
    :topics: 03-conditional/03-conditionalEx
    :from_source: T
    :practice: T
    :answer_a: all values of x
    :answer_b: 1 to 9
    :answer_c: 0 to 9
    :answer_d: 1 to 10
    :correct: a
    :feedback_a: This will be true if x is greater than 0 <b>or</b> less than 10.  This covers all possible values of x.
    :feedback_b: Try again. This would be true if the logical expressions were joined with and instead of or.
    :feedback_c: Try again. This would be true if the logical expressions were jointed with and instead of or and if the first logical expression was x >= 0.
    :feedback_d: Try again. This would be true if the logical expressions were jointed with and instead of or and if the first logical expression was x >= 0 and the second expression was <= 10.

    Given the code below, what describes the values of x that will cause the code to print "condition true"?

    ::

        if x > 0 or x < 10:
            print ("condition true")
        print ("All done")