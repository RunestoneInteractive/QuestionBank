.. mchoice:: functBuiltin_MC_min
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-builtin
    :topics: 04-functions/04-builtin
    :from_source: T
    :practice: T
    :answer_a: There is no minimum character because there are no numbers in this string.
    :answer_b: We named the variable a reserved keyword (minimum).
    :answer_c: The minimum character is a space. It prints but we just can't tell.
    :answer_d: 'Hello world' needs to be put in double quotes.
    :correct: c
    :feedback_a: Try again! There is a minimum character.
    :feedback_b: Minimum is not a reserved keyword.
    :feedback_c: The minimum character is a space, we cannot see it because the character was printed without quotes.
    :feedback_d: Strings can be in either single quotes ('') or double quotes ("").

    We see that w prints as the maximum character. How come it looks like the minimum does not print?

    .. code-block:: python

        maximum = max('Hello world')
        print(maximum)
        minimum = min('Hello world')
        print(minimum)