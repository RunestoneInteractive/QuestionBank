.. mchoice:: functBuiltin_MC_len
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-builtin
    :topics: 04-functions/04-builtin
    :from_source: T
    :practice: T
    :answer_a: 10
    :answer_b: 11
    :answer_c: 12
    :answer_d: 13
    :correct: d
    :feedback_a: Spaces and punctuation characters count in the length!
    :feedback_b: Punctuation characters count in the length!
    :feedback_c: Spaces count in the length!
    :feedback_d: 13 is the length of all characters in the string.

    Consider the code block below. What prints?

    .. code-block:: python

        sentence_a = "Hello, world!"
        length_sentence_a = len(sentence_a)
        print(length_sentence_a)