.. mchoice:: str-ex-mc-name
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: Mali is Mali
    :answer_b: Mali is 5
    :answer_c: 5 is Mali
    :answer_d: 5 is 5
    :correct: b
    :feedback_a: There are no double quotes around the last Mali so it will use the value of the variable Mali.
    :feedback_b: The first Mali is in double quotes so it will print the string Mali and the second Mali is not in double quotes so it will print the value of the variable Mali.
    :feedback_c: The first Mali is in double quotes and the second is not.
    :feedback_d: The first Mali is in double quotes so it is a string and the characters in the string will be printed.

    What would the following code print?

    ::

      Mali = 5
      print("Mali" + " is " + str(Mali))