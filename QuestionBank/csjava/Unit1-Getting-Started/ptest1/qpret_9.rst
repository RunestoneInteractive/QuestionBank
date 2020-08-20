.. mchoice:: qpret_9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit1-Getting-Started
    :subchapter: ptest1
    :topics: Unit1-Getting-Started/ptest1
    :from_source: F
    :answer_a: (c || d)
    :answer_b: (c && d)
    :answer_c: (!c) && (!d)
    :answer_d: !(c && d)
    :answer_e: (!c) || (!d)
    :correct: c
    :feedback_a: NOTing an OR expression does not result in the same values ORed.
    :feedback_b: You do negate the OR to AND, but you also need to negate the values of d and d.
    :feedback_c: NOTing (negating) an OR expression is the same as the AND of the individual values NOTed (negated). See De Morgans laws.
    :feedback_d: This would be equivalent to (!c || !d)
    :feedback_e: This would be equivalent to (!(c && d))

    Which of the following expressions is equivalent to the following?

    .. code-block:: java

        !(c || d)