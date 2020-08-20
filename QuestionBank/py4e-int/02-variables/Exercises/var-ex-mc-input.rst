.. mchoice:: var-ex-mc-input
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: Exercises
    :topics: 02-variables/Exercises
    :from_source: T
    :practice: T
    :answer_a: &lt;class 'str'&gt;
    :answer_b: &lt;class 'int'&gt;
    :answer_c: &lt;class 18&gt;
    :answer_d: 18
    :correct: a
    :feedback_a: All input from users is read in as a string.
    :feedback_b: Even though the user typed in an integer, it does not come into the program as an integer.
    :feedback_c: 18 is the value of what the user typed, not the type of the data.
    :feedback_d: 18 is the value of what the user typed, not the type of the data.

    What is printed when the following statements execute?

    .. code-block:: python

      n = input("Please enter your age: ")
      # user types in 18
      print ( type(n) )