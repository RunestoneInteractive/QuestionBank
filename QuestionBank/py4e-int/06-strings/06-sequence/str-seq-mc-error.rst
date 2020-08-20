.. mchoice:: str-seq-mc-error
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-sequence
    :topics: 06-strings/06-sequence
    :from_source: T
    :practice: T
    :answer_a: IndexError
    :answer_b: TypeError
    :answer_c: SyntaxError
    :correct: b
    :feedback_a: You will get an IndexError if you try to access a string beyond its range. For example, if string = "hi", calling string[2] would cause an IndexError.
    :feedback_b: A TypeError would occur because the program is expecting an integer as the index, not a float.
    :feedback_c: A SyntaxError is caused when there are issues with the code as it is written, rather than the values it is given.

    The following code would cause what kind of error?

    ::

        fruit = 'papaya'
        letter = fruit[1.5]