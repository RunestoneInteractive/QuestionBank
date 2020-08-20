.. mchoice:: itContinue_MC_letter
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-continue
    :topics: 05-iterations/05-continue
    :from_source: T
    :answer_a: Current Letter : P
    :answer_b: Current Letter : y
    :answer_c: Current Letter : t
    :answer_d: Current Letter : h
    :correct: d
    :feedback_a: This will print.
    :feedback_b: This will print.
    :feedback_c: This will print.
    :feedback_d: Because continue sends the loop to the next iteration at h, it will not print "Current Letter: h"

    Which of the following statements does not print?

    .. code-block:: python

        for letter in 'Python':
            if letter == 'h':
                continue
            print ('Current Letter : ' + letter)