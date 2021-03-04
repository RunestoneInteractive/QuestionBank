.. mchoice:: assess_question1_11_11_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: T
    :multiple_answers:
    :answer_a: It creates a new copy of <code>d</code>.
    :answer_b: It creates a new dictionary which swaps the keys and values in <code>d</code>.
    :answer_c: It throws an error.
    :answer_d: It creates a new dictionary which maps each of <code>d</code>'s keys to itself.
    :answer_e: It creates a new dictionary which maps each of <code>d</code>'s values to itself.
    :correct: b
    :feedback_a: It is not exactly a copy.
    :feedback_b: Yes, <code>d[c]</code> gets the value from dictionary <code>d</code>  with key <code>c</code>. In dictionary <code>e</code>, we are putting <code>d[c]</code> as a key and value as <code>c</code>.
    :feedback_c: It is a valid code.
    :feedback_d: The key of dictionary <code>e</code> is different from that of <code>d</code>.
    :feedback_e: The value of dictionary <code>e</code> is different from that of <code>d</code>.
    :practice: T

    What does the following block of code do?

    .. sourcecode:: python

        d =  {'a': 2, 'b': 3, 'c': 1}
        e = {}
        for c in d:
            e[d[c]] = c
        print e