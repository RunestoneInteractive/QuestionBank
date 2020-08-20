.. mchoice:: functEx_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: Exercises
    :topics: 04-functions/Exercises
    :from_source: T
    :answer_a: Zap ABC jane fred jane
    :answer_b: Zap ABC Zap
    :answer_c: ABC Zap jane
    :answer_d: ABC Zap ABC
    :answer_e: Zap Zap Zap
    :correct: d
    :feedback_a: The code will not print the strings "jane" or "fred" only "Zap" or "ABC"
    :feedback_b: This would be correct if the call was fred() jane() fred()
    :feedback_c: The code will not print the strings "jane" or "fred" only "Zap" or "ABC"
    :feedback_d: jane() fred() jane() will print ABC Zap ABC
    :feedback_e: This would be correct if the call was fred() fred() fred()

    What will the following Python program print out? (Given that each word is on its own line)

    .. code-block:: python

        def fred():
            print("Zap")

        def jane():
            print("ABC")

        jane()
        fred()
        jane()