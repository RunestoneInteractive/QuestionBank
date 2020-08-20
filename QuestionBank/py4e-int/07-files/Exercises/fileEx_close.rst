.. mchoice:: fileEx_close
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: Exercises
    :topics: 07-files/Exercises
    :from_source: T
    :practice: T
    :answer_a: "myText".close()
    :answer_b: ref_file.close()
    :answer_c: close(ref_file)
    :answer_d: close("myText")
    :correct: b
    :feedback_a: The title of the file is a string and a string cannot be closed in Python.
    :feedback_b: This closes the file using the variable it has been assigned to.
    :feedback_c: The command close() needs to be called on the file's variable using dot notation.
    :feedback_d: The command close() needs to be called on the file's variable using dot notation.

    Which command below closes the already open file ``myText.txt`` if the following code has already been written?

    ::

        ref_file = open("myText.txt", "r")