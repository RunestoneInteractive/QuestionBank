.. mchoice:: str-ex-mc-hey
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: Hey
    :answer_b: hey
    :answer_c: HEY
    :correct: c
    :feedback_a: This would be correct if we had asked what the value of s3 was. What is the value of s1?
    :feedback_b: This would be true if we asked what the value of s2 was after the code executes.  What is the value of s1?
    :feedback_c: Strings are immutable, meaning they don't change.  Any function that changes a string returns a new string.  So s1 never changes unless you set it to a different string.

    What is the value of s1 after the following code executes?

    ::

      s1 = "HEY"
      s2 = s1.lower()
      s3 = s2.capitalize()