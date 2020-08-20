.. mchoice:: cndtnl-debug-mc-error2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-debugging
    :topics: 03-conditional/03-debugging
    :from_source: T
    :practice: T
    :answer_a: x >= 2 and y != 0 and (x/y) > 2
    :answer_b: x >= 2 and y != 0 and (x/y) > 2
    :answer_c: x >= 2 and (x/y) > 2 and y != 0
    :correct: c
    :feedback_a: Try again. This will evaluate to False because y = 0.
    :feedback_b: Try again. This will evaluate to False because y = 0.
    :feedback_c: Since y = 0, x/y will cause en erorr. The gaurd (y != 0) should be placed before that expression.

    Which of the following will cause an error if x = 6 and y = 0?