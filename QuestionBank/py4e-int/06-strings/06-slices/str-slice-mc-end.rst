.. mchoice:: str-slice-mc-end
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-slices
    :topics: 06-strings/06-slices
    :from_source: T
    :practice: T
    :answer_a: This is the end
    :answer_b: This
    :answer_c: his
    :correct: c
    :feedback_a: This would be true if we were printing the value of str and we hand't changed it on line 2.
    :feedback_b: This would be true if the first position was 1 and the substring included the character at the end position, but the first character in a string is at position 0 and the substring won't include the character at the last position.
    :feedback_c: This will return a string that starts at position 1 and ends at position 3.

    What will be printed when the following executes?

    ::

      str = "This is the end"
      str = str[1:4]
      print(str)