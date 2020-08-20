.. mchoice:: functType_MC_error
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-typeconversion
    :topics: 04-functions/04-typeconversion
    :from_source: T
    :practice: T
    :answer_a: When converting a letters to an int, we must remove the quotation marks.
    :answer_b: The int function is expecting a value that can be converted to an integer.
    :answer_c: We cannot print and call a function in the same line.
    :correct: b
    :feedback_a: This would only work if Hello was a variable name with a value of the correct type. For example, hello = '32'.
    :feedback_b: The int function expects a value that can be converted, strings cannot convert to integers.
    :feedback_c: This is actually possible! It worked with the first line.

    Why would we get an error in the following code block?

    .. code-block:: python

        print(int('32'))
        print(int('Hello'))