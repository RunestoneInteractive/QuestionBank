.. mchoice:: functDef_MC_order
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-definitionsanduses
    :topics: 04-functions/04-definitionsanduses
    :from_source: T
    :answer_a: The lyrics print like normal.
    :answer_b: We get a TypeError.
    :answer_c: We get a NameError.
    :answer_d: The program compiles but nothing prints.
    :correct: a
    :feedback_a: This doesn't cause an error because both functions are defined before repeat_lyrics is called.
    :feedback_b: This will not cause a TypeError.
    :feedback_c: This will not cause a NameError.
    :feedback_d: This will print something.

    Consider the code block below. What happens when you run this program?

    .. code-block:: python

        def repeat_lyrics():
            print_lyrics()
            print_lyrics()

        def print_lyrics():
            print("I'm a lumberjack, and I'm okay.")
            print('I sleep all night and I work all day.')

        repeat_lyrics()