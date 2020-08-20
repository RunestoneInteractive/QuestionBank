.. mchoice:: inLoops_MC_itVar
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-loops
    :topics: 05-iterations/05-loops
    :from_source: T
    :answer_a: itervar
    :answer_b: count
    :answer_c: Count
    :answer_d: list
    :correct: a
    :feedback_a: iterver is the iteration variable.
    :feedback_b: count is just a variable counting the iterations.
    :feedback_c: Count is a string printed after the loop.
    :feedback_d: This loop iterates through a list, but that is not the iteration variable.

    Which variable is the iteration variable in the code block?

    .. code-block:: python

        count = 0
        for itervar in [3, 41, 12, 9, 74, 15]:
            count = count + 1
        print('Count: ', count)