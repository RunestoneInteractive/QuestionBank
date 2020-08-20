.. mchoice:: listString_MC_join
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listsAndStrings
    :topics: 08-lists/08-listsAndStrings
    :from_source: T
    :practice: T
    :answer_a: HannahGraceOliviaRuth
    :answer_b: Hannah Grace Olivia Ruth
    :answer_c: Hannah, Grace, Olivia, Ruth
    :answer_d: We would get an error
    :correct: a
    :feedback_a: Because the delimiter is an empty string (not a space) the list would join without spaces.
    :feedback_b: The delimiter is an empty string, not a space.
    :feedback_c: The delimiter is an empty string, it does not add spaces and commas automatically.
    :feedback_d: This will print without causing an error.

    What would print when the following code executes?

    ::

      mylist = ['Hannah', 'Grace', 'Olivia', 'Ruth']
      delimiter = ''
      print(delimiter.join(mylist))