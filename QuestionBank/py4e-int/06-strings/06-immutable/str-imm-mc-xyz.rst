.. mchoice:: str-imm-mc-xyz
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-immutable
    :topics: 06-strings/06-immutable
    :from_source: T
    :practice: T
    :answer_a: xyz
    :answer_b: xyxyz
    :answer_c: xy xy z
    :answer_d: xy z
    :answer_e: z
    :correct: b
    :feedback_a: s1 will equal "xy" plus another "xy" then z at the end.
    :feedback_b: s1 contains the original value, plus itself, plus "z"
    :feedback_c: No spaces are added during concatenation.
    :feedback_d: No spaces are added during concatenation, and an additional "xy" should be
                 included at the beginning.
    :feedback_e: s1 was set to "xy" initially, so the final answer will be "xyxyz"

    Given the following code segment, what is the value of the string s1 after these are executed?

    ::

      s1 = "xy"
      s2 = s1
      s1 = s1 + s2 + "z"