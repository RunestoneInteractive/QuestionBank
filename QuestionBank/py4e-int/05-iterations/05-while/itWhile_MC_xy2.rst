.. mchoice:: itWhile_MC_xy2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-while
    :topics: 05-iterations/05-while
    :from_source: T
    :practice: T
    :answer_a: x = 2; y = 5
    :answer_b: x = 5; y = 2
    :answer_c: x = 4; y = 3
    :answer_d: x = 4; y = 2
    :correct: c
    :feedback_a: The values of x and y will change.
    :feedback_b: The conditions of the while loop will not allow this combination to occur.
    :feedback_c: The loop will terminate at x = 4 and y = 3 because at this point, x is not less than y.
    :feedback_d: This loop will terminate before x = 4 and y = 2 because x has already been greater than y.

    Consider the code block below. What are the values of x and y when this while loop finishes executing?

    .. code-block:: python

        x = 2
        y = 5

        while (y > 2 and x < y):
            x = x + 1
            y = y - 1