.. mchoice:: str-seq-mc-name
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-sequence
    :topics: 06-strings/06-sequence
    :from_source: T
    :practice: T
    :answer_a: "s"
    :answer_b: " "
    :answer_c: "Olivia"
    :correct: a
    :feedback_a: Correct! In Python, counting starts with zero; so after the reassignment hello the 12th
                 character from the original string, "s".
    :feedback_b: Remember that in Python, counting starts at zero! And watch out for the reassignment.
    :feedback_c: Remember that in Python, counting starts at zero! And watch out for the reassignment.

    What is printed by the following statements?

    ::

        hello = "Hi my name is Olivia."
        hello = hello[12]
        print(hello)