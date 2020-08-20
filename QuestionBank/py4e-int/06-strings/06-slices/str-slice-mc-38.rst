.. mchoice:: str-slice-mc-38
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-slices
    :topics: 06-strings/06-slices
    :from_source: T
    :answer_a: python
    :answer_b: rocks
    :answer_c: hon r
    :answer_d: Error, you cannot have two numbers inside the [ ].
    :correct: c
    :feedback_a: That would be s[0:6].
    :feedback_b: That would be s[7:].
    :feedback_c: Yes, start with the character at index 3 and go up to but not include the character at index 8.
    :feedback_d: This is called slicing, not indexing.  It requires a start and an end.


    What is printed by the following statements?

    .. code-block:: python

      s = "python rocks"
      print(s[3:8])